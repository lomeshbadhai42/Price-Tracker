from bs4 import BeautifulSoup
import requests
import smtplib
import ssl
from email.message import EmailMessage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.conf import settings
def home(request):
    return render(request, 'main_app/home.html')

def contact(request):
    return render(request, 'main_app/contact.html')

def scrape_product_details(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        #Scrapping Product details
        name = soup.find('span', {'class':'B_NuCI'}).text.strip()
        item_price = soup.find(class_="_30jeq3 _16Jk6d").text[1:].split(',')
        price = int("".join(item_price))
        image = soup.find('div', {'class': '_3kidJX'}).find('img').get('src') 
        return {'name': name, 'price': price, 'image': image}
    
    except Exception as e:
        print(f"Error scraping product details: {e}")
        return None
    
@login_required
def search(request):
    if request.method == "POST":
        item_url = request.POST.get("searchbox")
        maximum_price = int(request.POST.get("max_price"))
        if item_url !="" and maximum_price !="":
            user = request.user
            item_model = Item(
                user = user, 
                url = item_url, 
                max_price = maximum_price,
                product_price = scrape_product_details(item_url)['price'], 
                product_name = scrape_product_details(item_url)['name'],
                image_url = scrape_product_details(item_url)['image'],               
            )
            item_model.save()
            return redirect("search")
        
    return render(request, "main_app/search.html")


def send_mail():
    max_price = 500000
    hdr = {'User-Agent': 'Mozilla/5.0'}

    for element in Item.objects.all():
        if element.status == False:
            user = element.user
            user_email = user.email
            item_url = element.url
            max_price = element.max_price

            #Scrapping Product price
            product_price = scrape_product_details(item_url)['price']
            element.product_price = product_price

            # sending mail if product price is less or equal to max price
            if product_price <= max_price:
                port = 465  # For SSL
                smtp_server = "smtp.gmail.com"
                sender_email = settings.EMAIL_HOST_USER
                password = settings.EMAIL_HOST_PASSOWRD
                subject = 'BUY NOW!'
                message = f"""
                Price has Dropped! Buy your product now!
                Link: {item_url}
                          """
                em = EmailMessage()
                em['From'] = sender_email
                em['To'] = user_email#receiver_email
                em['Subject'] = subject
                em.set_content(message)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, user_email, em.as_string())
                    print("Message Sent")
                element.status = True
                element.save()
            element.save()

send_mail()
            

   
@login_required
def tracking(request):
    tracked_products = Item.objects.filter(user=request.user).order_by('-id')
    return render(request, 'main_app/tracking.html', {'tracked_products': tracked_products})


def remove_from_tracking(request, pk):
    tracked_product = get_object_or_404(Item, pk=pk)
    tracked_product.delete()
    return redirect('tracking')
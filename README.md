# Frito-Restaurant

**Frito-Restaurant** is a full-stack restaurant management platform designed to provide a seamless online meal ordering experience for clients and efficient order management for administrators. With a user-friendly interface, advanced tracking features, and secure backend, it bridges the gap between customers and restaurant staff.

---

## 🌟 Key Features

### For Clients
- **Meal Ordering**: Choose from a wide range of meal categories, spices, and drinks.
- **Flexible Quantity**: Order meals in any amount with customizations.
- **Address Input**: Provide a GPS location or manually enter an address for delivery.
- **Mobile Number Integration**: Simplifies communication for takeaway and delivery.

### For Admins
- **Order Tracking**: View and process customer requests in real-time.
- **User Management**: Track user activities and manage order history.
- **Secure Backend**: Admin panel protected with encrypted user credentials.

### Advanced Features
- **WebSocket Integration**: Enables real-time updates for orders and admin notifications.
- **API Support**: Ensures seamless integration and scalability.
- **SSL-Enabled**: Provides a secure connection for all website interactions.

---

## 🔒 Why Choose Frito-Restaurant?
- **Modern UI/UX**: Designed for an intuitive experience for both clients and admins.
- **Secure Transactions**: (PBKDF2 with SHA256) encryption for passwords and sensitive data.
- **Comprehensive Features**: Covers the entire process from ordering to delivery.
- **Scalable Architecture**: Built with robust frameworks and technologies.

---

## 📚 Technologies Used

- **Frontend**:
  - HTML, CSS, Bootstrap: Responsive and visually appealing design.
  - jQuery: Dynamic and interactive user interface.

- **Backend**:
  - Django: Secure and scalable server-side framework.
  - SQLite: Lightweight and efficient database.

- **Other Tools**:
  - WebSockets: Real-time communication for updates.
  - SSL: Secure website communication.

---

## 💡 Get Started

### Clone the Repository
```bash
git clone https://github.com/yourusername/Frito-Restaurant.git
```

### Set Up the Environment
1. Install Python and required dependencies.
2. Set up the SQLite database by running migrations.
3. Configure API keys and SSL certificates (if applicable).

### Build and Run the Application
1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
2. Access the website at `http://127.0.0.1:8000/`.

### For SSL You Have To Install the certificate stored in certs folder if you want to change domain checkout on web how to create ssl current domain is frito-restraunt.com note it's a wild card certificate
1. Now After Enabling Venv by 
  ```bash
 ./venv/Scripts/Activate 
   ```
2. Go to Frito_Restraunt by
  ```bash
 cd Frito_Restraunt
   ```
3. Keep In Mind the local ip of your pc
3. Run the Project By 
 ```bash
  ../venv/Scripts/python.exe manage.py runsslserver  yourip:443 --certificate "/certs/certificate.crt" --key "/certs/key_nopass.pem"
   ```
---
## 🌐 Use Cases

- **Online Meal Ordering**: Clients can browse, customize, and order meals effortlessly.
- **Efficient Order Processing**: Admins can manage orders, track requests, and update statuses.
- **Delivery Coordination**: Clients provide accurate addresses or GPS locations for smooth deliveries.

---

**Frito-Restaurant** redefines the online dining experience with its powerful features and elegant design. Whether you're a client ordering your favorite meal or an admin managing a bustling kitchen, this platform ensures efficiency, security, and satisfaction for all.

# Fahdjud Auction Platform

A Django-based auction platform where users can create listings, place bids, add items to their watchlist, and interact through comments.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Create Listings**: Users can create auction listings with:
  - Title and description
  - Starting price
  - Category
  - Image URL
- **Bidding System**: Place bids on active listings with validation to ensure bids exceed current prices
- **Watchlist**: Save favorite listings for quick access
- **Categories**: Browse listings by category
- **Comments**: Add comments to listings
- **Listing Management**: Owners can close their listings

## Tech Stack

- **Framework**: Django 3.2+
- **Database**: SQLite (default) - easily configurable for PostgreSQL/MySQL
- **UI Components**: Django Cotton + shadcn-django
- **Styling**: Tailwind CSS

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fahdjud.git
   cd fahdjud
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Copy `.env.example` to `.env` and configure your settings:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and set:
   - `SECRET_KEY`: Generate a secure secret key
   - `DEBUG`: Set to `True` for development, `False` for production
   - `ALLOWED_HOSTS`: Add your domain names (comma-separated)
   - `CSRF_TRUSTED_ORIGINS`: Add trusted origins for CSRF protection

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load initial categories (optional)**
   
   You can add categories through the Django admin panel or create a data fixture.

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://localhost:8000` in your browser.

## Usage

### For Regular Users

1. **Register**: Create an account to start using the platform
2. **Browse Listings**: View all active auction listings on the homepage
3. **Filter by Category**: Browse listings in specific categories
4. **View Details**: Click on a listing to see full details, current bid, and comments
5. **Place Bids**: Enter a bid amount higher than the current price
6. **Add to Watchlist**: Save interesting listings to your watchlist
7. **Comment**: Share your thoughts on listings

### For Sellers

1. **Create Listing**: Click "Create Listing" to auction an item
2. **Set Details**: Add title, description, starting price, category, and image
3. **Monitor Bids**: See all bids placed on your listings
4. **Close Listing**: When ready, close the listing to end the auction

### Admin Panel

Access the admin panel at `http://localhost:8000/admin` to:
- Manage users
- Add/edit categories
- Moderate listings and comments
- View all bids

## Project Structure

```
.
├── auctions/              # Main application
│   ├── models.py          # Database models (User, Listing, Category, Comment, Action)
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── templates/         # HTML templates
│   └── static/            # Static files (CSS, JS, images)
├── commerce/              # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py            # WSGI configuration
├── templates/             # Shared templates
├── static/                # Global static files
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
└── README.md              # This file
```

## Database Models

- **User**: Extended Django user model
- **Category**: Listing categories
- **Listing**: Auction listings with title, description, price, owner, category, and active status
- **Comment**: User comments on listings
- **Action**: Bid records with price and timestamp

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Required |
| `DEBUG` | Debug mode | `False` |
| `ALLOWED_HOSTS` | Allowed hostnames | `localhost,127.0.0.1` |
| `CSRF_TRUSTED_ORIGINS` | Trusted origins for CSRF | `http://localhost:8000` |

## Security Notes

- **Never commit** the `.env` file to version control
- **Never commit** `db.sqlite3` - it may contain sensitive user data
- Generate a strong `SECRET_KEY` for production
- Set `DEBUG=False` in production
- Use HTTPS in production and update `CSRF_TRUSTED_ORIGINS` accordingly
- Consider using a production database (PostgreSQL/MySQL) instead of SQLite

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with Django
- UI components powered by Django Cotton and shadcn-django
- Styled with Tailwind CSS

## Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Note**: This is a learning/portfolio project. For production use, additional security hardening, testing, and optimizations are recommended.

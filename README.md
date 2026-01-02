# Django API Project - ORM Practice

## Features
- Custom QuerySet & Manager
- Chainable queries: paid().last_30_days()
- select_related & prefetch_related verified via Debug Toolbar
- Annotations & Subquery for total_paid
- Only APIs, no HTML pages

## API Endpoints
- GET /api/invoices/ → List invoices with customer name
- GET /api/customers/ → List customers with total_paid

## Verification
- Debug Toolbar SQL panel confirms ORM optimization
- Chain queries tested in Django shell

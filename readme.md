# Portfolio Website

## Overview

This portfolio website showcases your projects and provides a contact page for visitors to reach out to you. It includes features like template inheritance, project listing and detail views, and a dashboard for managing inquiries.

## Features

1. **Template Inheritance**: Utilizes Django template inheritance for consistent design across all pages.
2. **Contact Page**: Allows visitors to contact you by providing their email, full name, subject, and message.

3. **Project Views**:

   - **List View**: Displays a list of projects with an image, truncated description, and date posted.
   - **Detail View**: Shows a detailed view of a project with a carousel of images, a full description, and a button to redirect to the project website.

4. **CRUD Functionality**:

   - **Create, Update, Delete Views**: For managing projects, accessible only to the website owner.

5. **Dashboard**: A simple dashboard to list and manage inquiries received from the contact page.

## Technologies Used

- Django
- HTML/CSS
- JavaScript (for carousel functionality)
- Bootstrap (for responsive design)

## Notes

- No need to add Create View, Update View, and Delete View as it is built-in in Django

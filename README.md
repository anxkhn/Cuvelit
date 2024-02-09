# Cuvelit

![Cuvelit](https://raw.githubusercontent.com/anxkhn/Cuvelit/main/cuvelit.jpg)

## Introduction

Cuvelit, derived from "Cuvette" and "lit", symbolizes a lit af way to hunt to job opportunities. This project provides a simplified wrapper for accessing job listings from the Cuvette platform without the need for user authentication. The motivation behind this project is to provide free access to job information without subjecting users to intrusive dark patterns, affiliate links, or unnecessary login requirements imposed by the Cuvette website.

### Why Cuvelit?

Cuvette is a platform notorious for employing dark patterns and barriers to accessing job listings. Users are forced to create accounts, endure tracking, and navigate through affiliated links just to view job opportunities. It makes sense if Cuvette hosts their own opportunities, but it frequently redirects users to external company career sites, adding unnecessary complexity to the job search process and gatekeeping links for cold sign-ups. Cuvelit challenges these practices by offering a straightforward alternative for users to explore job opportunities.

## Features

- **No Forced Logins**: Users are not required to create accounts to access job listings.
- **No Tracking**: Cuvelit does not use bloated JS or collect user data.
- **Direct Access to Job Listings**: Users can directly access job listings without being redirected to external sites.
- **Promotion of Free Information**: Cuvelit advocates for free and accessible job information for everyone.

## API Documentation

### Endpoint

- **Base URL**: `https://api.cuvette.tech/api/v1/externaljobs`

### Response Format

The API response follows a consistent JSON format:

```json
{
  "success": true,
  "count": 420,
  "data": [
    {
      "_id": "65c4b92b5c74a6201c1d87a6",
      "companyName": "Honeywell",
      "title": "Software Engineer I",
      "location": "Hyderabad",
      "imageUrl": "data:image/png;base64,",
      "type": "In-Office Job",
      "salary": "Salary: 13 LPA - 18 LPA",
      "redirectLink": "https://careers.honeywell.com/us/en/job/HRD221192/",
      "requiredExperience": "0-2 years",
      "skills": "Java, React, Node",
      "createdAt": "2024-02-08T11:21:12.714Z",
      "updatedAt": "2024-02-09T14:23:38.757Z",
      "aboutJob": "",
      "count": 8488
    },
    {
      "_id": "65c2250d27b1ff799f997980",
      "companyName": "Zoho",
      "title": "Software Developer",
      "location": "Chennai",
      "imageUrl": "data:image/png;base64,",
      "type": "In-Office Job",
      "salary": "Salary: 5 LPA - 8 LPA",
      "redirectLink": "https://careers.zohocorp.com/forms/fcc89b5ebd373d598e0224d10f2199d1a8839a1914d1ba3a141e0b0ddcfcfc32",
      "requiredExperience": "0-2 years",
      "skills": "C, C++, Java",
      "createdAt": "2024-02-06T12:24:42.708Z",
      "updatedAt": "2024-02-09T14:23:21.992Z",
      "aboutJob": "",
      "count": 13929
    }
    // ....
  ]
}
```

### Data Structure

- `success` (boolean): Indicates whether the API request was successful.
- `count` (integer): Total count of job listings returned.
- `data` (array): Array containing job listing objects.
  - `_id` (string): Unique identifier for the job listing.
  - `companyName` (string): Name of the hiring company.
  - `title` (string): Title of the job position.
  - `location` (string): Location of the job.
  - `imageUrl` (string): URL to the image associated with the job (base64 encoded).
  - `type` (string): Type of job (e.g., In-Office Job, Remote Job).
  - `salary` (string): Salary range for the job position.
  - `redirectLink` (string): URL redirecting to the detailed job description.
  - `requiredExperience` (string): Required experience for the job position.
  - `skills` (string): Required skills for the job position.
  - `createdAt` (string): Date and time when the job listing was created.
  - `updatedAt` (string): Date and time when the job listing was last updated.
  - `aboutJob` (string): Brief description about the job.
  - `count` (integer): Number of applications or interactions with the job listing.

### Notes

- The `redirectLink` field directs users to the detailed job description hosted on the company's career page.
- Images associated with job listings are encoded as base64 strings.
- The API response provides essential details about each job listing, including company name, job title, location, salary, required experience, skills, and more.

## Getting Started

You can get started with this project either by using the deployed version available at [Cuvelit.dev.pages](https://Cuvelit.dev.pages) or deploying your own version.

### Deployed Version (Recommmeneded)

To use the deployed version from [Cuvelit.dev.pages](https://Cuvelit.dev.pages), simply visit the website and start exploring job listings.

### Getting Started Locally

If you prefer to set up the project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/anxkhn/Cuvelit
```

2. Navigate to the project directory:

```bash
cd Cuvelit
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask application:

```bash
flask run
```

## Contributing

Contributions to this project are welcome and encouraged. If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## Disclaimer

This project is not affiliated with Cuvette or any of its associated entities. It is a community-driven effort to promote transparency and accessibility in the job search process.

## License

This project is licensed under the [GPL v3 License](https://github.com/anxkhn/Cuvelit/LICENSE).

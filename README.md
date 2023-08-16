# Scrapper-WDET
 PythonJobRecommender 

https://docs.google.com/document/d/1W9jJToDuHpyT4_hqVWEw92C-5eYGojLxO1A_28dDWSE/edit?usp=sharing
 

Scraping 
Web scraping is the process of gathering data for the web in an automated way without interacting with the APIs. The most common way of accomplishing this is through sending a data request to web servers and parsing the received data. 

Compared to browsers, web scrapers can interact with many pages and servers simultaneously to gather and gather more data. 

In this project, we have implemented a scraper that gathers job details from popular job listing sites like LinkedIn, Monster, and Indeed. This information is matched with the candidate's resume to recommend the most suitable jobs. 

The vital detail to consider when scraping data from different websites is understanding how the data is organized. This is achieved by looking at the HTML DOM structure of each site’s pages that house the data we seek. 

For the project, we implement scraping in two stages. 
First on the jobs home page where all the jobs are listed. Although the jobs listed contain information like the position, location, a brief description of the job role, and the company offering the job, we need more information about the job role to make efficient recommendations to the users. Hence we only scrape for the link of the complete job details page in the first step.
 
Second, we iterate through all the links collected in the first step and open the links to get the complete job description, along with the company name position, and location. The figures below indicate the details on the job detail page. We can see that the page has an enormous amount of description that is useful for recommendations.



 

Flow diagram of search home page and detail page process

Libraries
I have listed below the python libraries I have used to scrape and process the data from the web. 
Beautifulsoup
Beautifulsoup is the library used for extracting the data from HTML. Beautifulsoup works with a parser to navigate, extract, search, and modify the HTML parse tree. 

For this project, we make use of Beautifulsoup for all the activities mentioned above. 
Methods, Objects, and Properties
Beautifulsoup provides various methods, objects, and object properties to perform searching, extracting, and modifying the data from the parse tree. 
Element.find_all() 
find_all() method looks through all the descendants of a tag and retrieves all those that match the filter conditions in a list. The list can be iterated over to process each element further. Filter conditions can also be added using the element properties to restrict the retrieved elements. Filters can be based on class names, attribute values, tag properties, etc.



Element.filnd() 
find() is similar to find_all() in many ways. find() supports all the filter properties mentioned in the find_all(). find() only returns a single result scanning the document or the element’s dependents. 
Element.Tag_Name 
A tag is an object that corresponds to HTML tags like <body>, <a>, <b> etc. The tag object provides various properties to access the HTML tag attributes and name. 
Selenium
Selenium is an open-source project that provides various browser automation functions supporting various languages. It is mainly used for automation testing, browser automation, or control through code for clicking buttons, scrolling and taking screenshots, etc.

In this project, we use selenium library functions to scroll the job search pages so more job posts are loaded. The job sites LinkedIn and Moster don't support pagination, instead, they load more jobs as and when the user reaches the end of the page going through the entire list of jobs. It is a dynamic way of providing paginations. Hence we use selenium as it provides a browser automation feature. We can see the literary opening the browser, scrolling through the jobs page, and closing once enough jobs are loaded. 

Selenium uses the WebDriver protocol to control web browsers like Chrome, Firefox, or Safari. The browser can run either locally or remotely. For our project, we make use of the Chrome web driver. 
Methods, Objects, and Properties
Element.get(URL)
Open the URL is the web driver specified. 
Element.find_element_by_class_name(name)
To find the element in the web page with the specified value for the class name 
ActionChains.move_to_element()
To scroll until the element specified is visible on the browser screen.

Concurrent Features
This library is used to implement threading in Python. Threading is executing the non-dependent functions in a program in an asynchronous parallel way independent of one another. Each such independent execution path is referend as a thread. Since threads run in parallel simultaneously, they result in faster program completion. 

In the project, we use ThreadPoolExecutor() of the concurrent features to start parallel processing LinkedIn, Indeed, and Monster. The total time taken for processing all the job sites is equal to processing a single more time-consuming task.

Multithreaded vs sequential process concerning the time
Requests 
Requests literary allows you to send HTTP requests to the specified server and receive the response. The response is stored and processed by beautifulsoup. The requests library is much simpler and requires fewer system resources, hence whenever scrolling, clicking is not required requests library is implemented. The complete process of scraping jobs from the search home page and the complete details from the job detail page for Indeed is achieved using the requests library features. 
Other Libraries
CSV 
We have used the CSV library to store the information gathered from scrapping the job sites. The results will be stored in the CSV format. Storing the results in the comma-separated values format is simple and less resource-intensive. The recommendation system will utilize this to match the most appropriate jobs. 

The result has the following columns 
ID: A unique number to identify the job posting and its details 
Job Title: Stores the role offered. 
Company: The name of the organization that has posted the job offer
Job Page Link: URL link to the job detail page to apply to the job
Job Description: The complete description of the job from the job details page. 
Source: The name of the job search site from with the job was retrieved. 


Screenshot of the CSV file 
Time 
Time library gives time-related functionalities like current time, sleep, etc. In this project, the time function is mainly used with selenium to add time delays in the program during page loading. Adding a time delay after each browser action ensures we provide the browser enough time to load before starting to scrape. 

LinkedIn 
Linkedin is a social network primarily focused on professional networking, career development, and job seeking. As I explained at the beginning of the document we are concerned with two pages on each website, first the job search page and then the job detail page. 
Job Search Page
We enter the search page by building the URL with the entered position and location. On the search page, the jobs are organized using unordered lists. Each list contains a job card with a link to the job detail page. While scraping we use the find_all() method of beautiful soup with class name filters to get all the anchor tags in the unordered list. Each tag is iterated over to extract the job detail page link. The extracted links are stored in an array.  

LinkedIn Search Page 


DOM structure organization of LinkedIn Search Page 


LinkedIn Search page scraping code 

LinkedIn doesn't provide pagination to allow users to go to the next page to look for more jobs. Instead, LinkedIn provides an unlimited scrolling option where the users can scroll down the search page and load more jobs. We achieve the process of scrolling by executing the window.scroll() script in Selenium’s execute_script method. 

Job Detail Page
Once we have the links array we iterate through each of the links. We open the detail page by sending a query to the server using requests library’s requests.get(URL) method. 


Mappings 
Link: Class Name = base-card__full-link of Anchor tag
Description: Class Name = show-more-less-html__markup on Div tag
Position: Class Name = show-more-less-html__markup on H2 tag
Company: Class Name = topcard__org-name-link on Anchor tag
Monster 
Monster is a popular career site, many professional and multinational companies use this to search for jobs and post opportunities. 
Scraping Process
The search page is organized using simple div blocks arranged one below another. Monster also doesn't provide pagination but follows a similar approach to LinkedIn, where users can scroll the site to load more jobs. The only difference is that the scrolling must be made on the inner element that lists all the jobs and not the whole browser window as in LinkedIn. This is carried out using the move_to_element of the action chains method of Selenium. Here we set the target to be at the load more button at the bottom.

Here we scrape the Company, Position, and Link from the job card in the search page and use the detail page only to scrape the job description. 

Once we have the links we follow a similar process to LinkedIn and open the details page iteratively to scrape the description. 

Mappings 
JobCard: Class Name = job-cardstyle__JobCardComponent-sc-1mbmxes-0 on Article tag
Description: All text is the Main tag of the detail page
Position: Anchor tag of the main Job Card 
Company: H3 tag of the main Job Card
Indeed
Indeed is similar to monster where job seekers and companies seeking professionals primarily use it. 
Scraping Process
The basic process is similar to the other websites where the job detail page links are scraped from the listings page and the details like company name, position, and description are scraped from the detail page. 

The significant difference on Indeed is that it provides pagination to look for more jobs hence we only make use of the requests library to do the complete scraping as we do not need to scroll to load more jobs. In such a case while building the base page URL, we can also specify the pagination page number. 

We process the pagination links to scrape the job links; one we have the required number of links for the detail page, we open the job detail page iteratively and scrape the company, position, and description.
Mappings 
Link: Id Value = mosaic-provider-jobcards on Div tag
Description: Class Name = jobsearch-JobComponent-description on Div tag
Position: Class Name = jobsearch-JobInfoHeader-title-container on H2 of the Div tag
Company: Class Name = jobsearch-CompanyInfoContainer on the string of first non empty child of Div tag







<h1 align="center">Comments</h1>
<p align="center">Collection of REST APIs to perform CRUD operations on comments resource, built using <a href="https://www.djangoproject.com" target="_blank">Django</a>, <a href="https://www.django-rest-framework.org" target="_blank">Django REST Framework</a> and <a href="https://www.postgresql.org" target="_blank">PostgreSQL</a> as data source.</p>
<p align="center">A <a href="https://shielded-reef-84687.herokuapp.com" target="_blank">demo</a> is deployed on Heroku.</p>

## REST Endpoints

| Path                | Method |                            Description |
| ------------------- | :----: | -------------------------------------: |
| /comments           |  GET   |                   Get list of comments |
| /comments           |  POST  |                     Create new comment |
| /comments/1         |  GET   |    Get details of a particular comment |
| /comments/1         |  PUT   | Update details of a particular comment |
| /comments/1         | DELETE |            Delete details of a comment |
| /comments/1/replies |  GET   |               Get replies on a comment |
| /replies            |  GET   |                    Get list of replies |
| /replies/1          |  PUT   |                         Update a reply |
| /replies/1          | DELETE |                         Delete a reply |

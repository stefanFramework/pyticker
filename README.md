# PyTicker 

1. **Configure Environment Variables**:

   - Create a `.env` file on the project root:

     ```bash
     touch .env
     ```

   - Open the `.env` file with a text editor and set the environment variables as needed. Below is a description of the key variables:
     - `ENV`: The environment in which the app is running; typically `DEV`, `TEST` or `PROD`.
     - `SQLALCHEMY_DATABASE_URI`: The database connection URL. For example, for a PostgreSQL database: `postgresql://user:password@localhost:port/database_name`.

     Ensure that the `SQLALCHEMY_DATABASE_URI` matches the database configuration specified in the `docker-compose.yml` file if you're using Docker for the database service.

2. **Start the Application with Docker**:

   - Build and start the Docker containers:

     ```bash
     docker-compose up --build
     ```

     This command will build the Docker images and start the services defined in the `docker-compose.yml` file. By default, this includes the Flask application and a PostgreSQL database.

   - To stop the services:

     ```bash
     docker-compose down
     ```

     This command stops and removes the containers defined in the `docker-compose.yml` file.


## License

This project is licensed under the AGPL-3.0 License. See the [LICENSE](LICENSE) file for details.


  

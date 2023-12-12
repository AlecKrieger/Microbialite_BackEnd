from fastapi import FastAPI

# Load environment variables from the .env file
app = FastAPI()

from routes.TicketRoutes import router as ticketRouter
from routes.UserRoutes import userRouter, analystRouter

app.include_router(ticketRouter)
app.include_router(userRouter)
app.include_router(analystRouter)
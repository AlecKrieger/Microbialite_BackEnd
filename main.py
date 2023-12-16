from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Load environment variables from the .env file
app = FastAPI()
origins = [
    "http://localhost",
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routes.TicketRoutes import router as ticketRouter
from routes.UserRoutes import userRouter, analystRouter
from routes.AdminRoutes import router as adminRouter
from routes.WaypointRoutes import router as WaypointRouter
from routes.MacroRoutes import router as MacroRouter
from routes.MesoRoutes import router as MesoRouter
from routes.ThinSectionRoutes import router as ThinSectionRouter
from routes.ReportRoutes import router as ReportRouter

app.include_router(ReportRouter)
app.include_router(ticketRouter)
app.include_router(userRouter)
app.include_router(analystRouter)
app.include_router(adminRouter)
app.include_router(WaypointRouter)
app.include_router(MacroRouter)
app.include_router(MesoRouter)
app.include_router(ThinSectionRouter)

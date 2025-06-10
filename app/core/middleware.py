import logging
import time
from fastapi import Request

logger = logging.getLogger(__name__)

async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    logger.info(f"Request: {request.method} {request.url}")
    logger.debug(f"Headers: {dict(request.headers)}")
    logger.debug(f"Query params: {dict(request.query_params)}")
    
    try:
        response = await call_next(request)
    except Exception as ex:
        logger.error(f"Request failed: {str(ex)}")
        raise
    
    process_time = (time.time() - start_time) * 1000
    formatted_time = f"{process_time:.2f}"
    
    logger.info(
        f"Response: {response.status_code} "
        f"(Time: {formatted_time}ms)"
    )
    return response
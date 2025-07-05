

@app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(400)
def bad_request(e):
    return render_template('400.html'), 400

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405

@app.errorhandler(410)
def gone(e):
    return render_template('410.html'), 410
@app.errorhandler(401)
def unauthorized(e):
    return render_template('401.html'), 401 
@app.errorhandler(408)
def request_timeout(e):     
    return render_template('408.html'), 408

@app.errorhandler(429)
def too_many_requests(e):       
    return render_template('429.html'), 429

@app.errorhandler(501)
def not_implemented(e):
    return render_template('501.html'), 501

@app.errorhandler(502)
def bad_gateway(e):
    return render_template('502.html'), 502
@app.errorhandler(503)
def service_unavailable(e):
    return render_template('503.html'), 503

@app.errorhandler(504)
def gateway_timeout(e): 
    return render_template('504.html'), 504

@app.errorhandler(418)
def teapot(e):  
    return render_template('418.html'), 418

@app.errorhandler(422)  
def unprocessable_entity(e):  
    return render_template('422.html'), 422

@app.errorhandler(423)  
def locked(e):
    return render_template('423.html'), 423

@app.errorhandler(424)  
def failed_dependency(e):   
    return render_template('424.html'), 424

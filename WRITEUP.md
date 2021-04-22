# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*
The correct choice for this application will be App service, since App service cost less than VM and since the CMS is just
lauching, App service will be a better fit when it comes to cost of deployment.
App service will also give room for scalling in the event that the service get more users or traffic.
With App service the service can easily be containerised which will give a better workflow.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 
If the application gets popular in the future and there is need to cater for vast increase of users, then it can be moved to a VM and also
if the owner wants to better handle/manage the application security, then VM will also be a better fit, Or if the owner wants to move to programming environment that is not supported by App service.
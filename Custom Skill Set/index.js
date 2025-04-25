module.exports = async function (context, req) {
    context.log('Employee ID Extractor function processed a request.');
    
    if (!req.body || !req.body.values || !Array.isArray(req.body.values)) {
        context.res = {
            status: 400,
            headers: { "Content-Type": "application/json" },
            body: { values: [] }
        };
        return;
    }
    
    const responseBody = {
        values: []
    };
    
    // Process each record
    for (const record of req.body.values) {
        // Get content from the record
        const recordId = record.recordId;
        const data = record.data;
        
        try {
            // Log what we're receiving to check the structure
            context.log(`Processing record ${recordId}`);
            context.log(`Content keys: ${Object.keys(data).join(', ')}`);
            
            // Get the content field
            const content = data.content || '';
            context.log(`Content length: ${content.length}`);
            
            // Extract employee IDs
            const regex = /EMP-\d{5}/g;
            const matches = content.match(regex) || [];
            const uniqueEmployeeIds = [...new Set(matches)];
            
            context.log(`Found employee IDs: ${uniqueEmployeeIds.join(', ')}`);
            
            // Add to response
            responseBody.values.push({
                recordId: recordId,
                data: {
                    employeeIds: uniqueEmployeeIds
                }
            });
        } catch (error) {
            context.log(`Error processing record ${recordId}: ${error.message}`);
            responseBody.values.push({
                recordId: recordId,
                errors: [{ message: error.message }],
                data: {
                    employeeIds: []
                }
            });
        }
    }
    
    context.res = {
        headers: { "Content-Type": "application/json" },
        body: responseBody
    };
    
    context.log('Function completed processing');
};
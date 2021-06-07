#Error Handler
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown): #checks if on cooldown
        msg1 = 'Still on cooldown, please try again in {:.2f}s.'.format(error.retry_after)
        await ctx.send(msg) 
    if isinstance(error, commands.MissingRequiredArgument): #checks if missing required args
      msg2 = "Please enter all the required arguments!"
      await ctx.send(msg2)
    if isinstance(error, commands.MissingPermissions): #checks if missing perms
      msg3 = "You are missing permissions to use that command!"
      await ctx.send(msg3)
    if isinstance(error, commands.CommandNotFound): #checks if command not found
      msg4 = "No command found!"
      await ctx.send(msg4)
    
#This is just a plain text version of the error handler you can make an embed version too.

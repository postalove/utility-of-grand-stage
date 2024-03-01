'''
Discord-Bot-Module template. For detailed usages,
 check https://interactions-py.github.io/interactions.py/

Copyright (C) 2024  __retr0.init__

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import interactions
# Use the following method to import the internal module in the current same directory
from . import internal_t

'''
Replace the ModuleName with any name you'd like
'''
class Functions(interactions.Extension):
    module_base: interactions.SlashCommand = interactions.SlashCommand(
        name="export",
        description="git Replace here for the base command descriptions"
    )
    module_group: interactions.SlashCommand = module_base.group(
        name="info",
        description="test some functions"
    )

    @module_group.subcommand("staff_members", sub_cmd_description="导出公职人员名单")
    
    async def module_group_ping(self, ctx: interactions.SlashContext):

        guild = ctx.guild
        result = ''
        await ctx.defer()
            
        for role in reversed(guild.roles):
            if role.name == '————-[Bot身份组]-————':
                break
            if role.name.startswith('——'):
                continue
            result = result + f'{role.name}:'
            
            for member in guild.members:
                
                
                # Check if the role is in the member's roles
                if role in member.roles:
                    result = result + f'{member.mention} '
            result = result + '\n'
                # If the role is '临时成员', break the loop
            
        embed = interactions.Embed(
        title="公职人员名单",
        description=result,
        color=0x00ff00  # You can change the color as desired
    )
        await ctx.send(embed=embed)
        

    '''@module_base.subcommand("pong", sub_cmd_description="Replace the description of this command")
    @interactions.slash_option(
        name = "option_name",
        description = "Option description",
        required = True,
        opt_type = interactions.OptionType.STRING
    )
    async def module_group_pong(self, ctx: interactions.SlashContext, option_name: str):
        await ctx.send(f"Pong {option_name}!")
        internal_t.internal_t_testfunc()'''
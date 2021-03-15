import React from 'react';
import {SidebarContainer, 
        Icon, 
        CloseIcon,
        SidebarWrapper,
        SidebarMenu,
        SidebarLink,
        SideBtnWrap,
        SidebarRoute}
from './SidebarElements';

const Sidebar = () => {
    return (
        <SidebarContainer>
           <Icon>
               <CloseIcon />
            </Icon> 
            <SidebarWrapper>
                <SidebarMenu>
                    <SidebarLink to='home'>Home</SidebarLink>
                    <SidebarLink to='overView'>OverView</SidebarLink>
                    <SidebarLink to='team'>Team</SidebarLink>
                    <SidebarLink to='howitworks'>How It Works</SidebarLink>
                    <SidebarLink to='signup'>Sign UP</SidebarLink>
                </SidebarMenu>
                <SideBtnWrap>
                    <SidebarRoute to="/signin">Sign In</SidebarRoute>
                </SideBtnWrap>
            </SidebarWrapper>
        </SidebarContainer>
    );
};

export default Sidebar;

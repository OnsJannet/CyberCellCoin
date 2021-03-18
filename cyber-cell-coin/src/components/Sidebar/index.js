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

const Sidebar = ({isOpen, toggle}) => {
    return (
        <SidebarContainer isOpen={isOpen} onClick={toggle}>
           <Icon onClick={toggle}>
               <CloseIcon />
            </Icon> 
            <SidebarWrapper>
                <SidebarMenu>
                    <SidebarLink to='home' onClick={toggle}>Home</SidebarLink>
                    <SidebarLink to='overView' onClick={toggle}>OverView</SidebarLink>
                    <SidebarLink to='team' onClick={toggle}>Team</SidebarLink>
                    <SidebarLink to='howitworks' onClick={toggle}>How It Works</SidebarLink>
                    <SidebarLink to='signup' onClick={toggle}>Sign up</SidebarLink>
                </SidebarMenu>
                <SideBtnWrap>
                    <SidebarRoute to="/signin">Sign In</SidebarRoute>
                </SideBtnWrap>
            </SidebarWrapper>
        </SidebarContainer>
    );
};

export default Sidebar;

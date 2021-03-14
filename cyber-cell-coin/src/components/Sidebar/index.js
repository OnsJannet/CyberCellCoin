import React from 'react';
import {SidebarContainer, 
        Icon, 
        CloseIcon,
        SidebarWrapper,
        SidebarMenu,
        SideBarLink,
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
                    <SideBarLink to="home">
                        Home
                    </SideBarLink>
                    <SideBarLink to="overView">
                        OverView
                    </SideBarLink>
                    <SideBarLink to="team">
                        Team
                    </SideBarLink>
                    <SideBarLink to="howitworks">
                        How It Works
                    </SideBarLink>
                    <SideBarLink to="signup">
                        Sign UP
                    </SideBarLink>
                </SidebarMenu>
                <SideBtnWrap>
                    <SidebarRoute to="/signin">Sign In</SidebarRoute>
                </SideBtnWrap>
            </SidebarWrapper>
        </SidebarContainer>
    );
};

export default Sidebar

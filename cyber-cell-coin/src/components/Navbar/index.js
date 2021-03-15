import React from 'react'
import {FaBars} from 'react-icons/fa'
import{
    Nav, 
    NavbarContainer, 
    NavLogo, 
    MobileIcon, 
    NavMenu, 
    NavItem, 
    NavLinks,
    NavBtn,
    NavBtnLink}
from './NavbarElemnts';



const Navbar = () => {
    return (
        <>
            <Nav>
                <NavbarContainer>
                    <NavLogo to='/'>CyberCell</NavLogo>
                    <MobileIcon>
                        <FaBars />
                    </MobileIcon>
                    <NavMenu>
                        <NavItem>
                            <NavLinks to='home'>Home</NavLinks>
                        </NavItem>
                        <NavItem>
                            <NavLinks to='overView'>OverView</NavLinks>
                        </NavItem>
                        <NavItem>
                            <NavLinks to='team'>Team</NavLinks>
                        </NavItem>
                        <NavItem>
                            <NavLinks to='howitworks'>How it works</NavLinks>
                        </NavItem>
                        <NavItem>
                            <NavLinks to='signup'>Sign UP</NavLinks>
                        </NavItem>
                    </NavMenu>
                    <NavBtn>
                        <NavBtnLink to="/signin">Sign In</NavBtnLink>
                    </NavBtn>

                </NavbarContainer>
            </Nav>
        </>
    );
};

export default Navbar;

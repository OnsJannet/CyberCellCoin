import React from 'react'
import{Nav, NavbarContainer, NavLogo} from './NavbarElemnts';



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
                            NavLinks to=''
                        </NavItem>
                    </NavMenu>

                </NavbarContainer>
            </Nav>
        </>
    );
};

export default Navbar

import React from 'react'
import {Nav, initializeIcons} from '@fluentui/re'
import * as FaIcons from 'react-icons/fa';
import {Link} from 'react-router-dom';
import { BigContainer, SidebarContainer, ChartContainer } from './DashboardElements'

const Dashboard = () => {
  return (
    <div>
      <BigContainer>
          <SidebarContainer>
            <Link to="#" className='menu-bars'>
              <FaIcons.FaBars/>
            </Link>
          </SidebarContainer>
          <ChartContainer></ChartContainer>
      </BigContainer>
    </div>
  )
}

export default Dashboard

import './index.scss';
import { useCallback } from 'react';
import { Outlet } from 'react-router-dom';
import Topbar from '../Topbar'


const Layout = () => {
    
    return (
    
      <div className="App">
        <Topbar/>    
        <div className='page'>
          <Outlet />
        </div>
      </div>
    );

};

export default Layout;
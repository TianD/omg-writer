import { Layout, Menu } from 'antd';
import { Link, Outlet } from 'react-router-dom';
import './Root.css'

const { Header, Content, Footer } = Layout;

const menu_items = [
    {
        key: 'discovery',
        label: <Link to="/">Discovery</Link>,

    },
    {
        key: 'myself',
        label: <Link to="/myself">Myself</Link>
    },
    {
        key: 'about',
        label: <Link to="/about">About</Link>
    },

]

function Root() {
    return (
        <div className="App">
            <Layout className="layout">
                <Header>
                    <div className="logo" />
                    <Menu
                        theme="dark"
                        mode="horizontal"
                        defaultSelectedKeys={['discovery']}
                        items={menu_items}
                    >
                    </Menu>
                </Header>
                <Content
                    style={{
                        padding: '0 50px',
                    }}
                >
                    <Outlet />
                </Content>
                <Footer
                    style={{
                        textAlign: 'center',
                    }}
                >
                    Ant Design ©2018 Created by Ant UED
                </Footer>
            </Layout>
        </div>

    );
}


export default Root
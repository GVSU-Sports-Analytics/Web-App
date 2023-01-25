import NavItem from "./NavItem"


const navContent = [

    {
        href: "/",
        text: "Home",
    },

    {
        href: "/baseball",
        text: "Baseball",
    },

    {
        href: "/softball",
        text: "Softball"
    },

    {
        href: "/",
        text: "About",
    },

    {
        href: "https://github.com",
        text: "GitHub",
    },
]


export default function Nav() {
    return (
        <div>
            <nav className="bg-white px-2 sm:px-4 py-2.5 dark:bg-gray-900 fixed w-full z-20 top-0 left-0 border-b border-gray-200 dark:border-gray-600">
                    <div className="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-sticky">
                        <ul className="flex flex-col p-4 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                            {navContent.map((item) => {
                                return (
                                    <NavItem 
                                    props={item}
                                    className="flex items-center"/>
                                )
                            })}
                        </ul>
                    </div>
            </nav>
        </div>
    )
}

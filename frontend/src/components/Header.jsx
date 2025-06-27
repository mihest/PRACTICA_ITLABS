

const Header = ({className}) => {
    return(
        <header className={`h-[164px] flex items-center ${className}`}>
            <img src="/logo.png" alt="logo"/>
            <div className="flex flex-col ms-[40px]">
                <span className="text-[64px]/[100%] text-[#2B2A29] font-bold">Музей Боевой и Трудовой Славы</span>
                <span className="text-[58px]/[100%] text-[#514F4D] font-bold">город Александров</span>
            </div>
        </header>
    )
}
export default Header;
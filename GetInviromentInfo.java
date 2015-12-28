
public class GetInviromentInfo {
	private static final String osName	=	System.getProperty("os.name");
	private static final String dataModel	=	System.getProperty("sun.arch.data.model");
	private static final String vmVersion	=	System.getProperty("java.vm.version");
	private static final String osArch	= 	System.getProperty("os.arch");

public static void main (String[] args){
	System.out.println("osName	= "+osName);
	System.out.println("dataModel 	= "+dataModel);
	System.out.println("vmVersion 	= "+vmVersion);
	System.out.println("osArch    	= "+osArch);
	System.out.println("========================")
	}
}

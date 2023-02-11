%%���γ������һ�������Һ���
%�����ҹ���ϵͳ
clear all;
close all;
Ts=1;
N_sample=17;        %�����������
dt=Ts/N_sample;     %����ʱ�����
df=1.0/(20.0*Ts);   %����Ƶ�ʷ���
t=-10*Ts:dt:10*Ts;
f=-2/Ts:df:2/Ts;
alpha=[0,0.5,1];
for n=1:length(alpha)
    for k=1:length(f)
        if abs(f(k))>0.5*(1+alpha(n))/Ts
            Xf(n,k)=0;
        elseif abs(f(k))<0.5*(1+alpha(n))/Ts
            Xf(n,k)=Ts;
        else
            Xf(n,k)=0.5*Ts*(1+cos(pi*Ts/(alpha(n)+eps)*(abs(f(k))-0.5*(1-alpha(n))/Ts)));  
            %�޲�����eps����ָ���Ǵ�1.0����һ���ϴ��˫������֮��ľ��룬�䷵��ֵΪ2^(-52)
        end
    end
    xt(n,:)=sinc(t/Ts).*(cos(alpha(n)*pi*t/Ts))./(1-4*alpha(n)^2*t.^2/Ts^2+eps);
end
figure(1);
plot(f,Xf(1,:),'b',f,Xf(2,:),'r',f,Xf(3,:),'k');
axis([-1 1 0 1.2]);xlabel('f/fs');ylabel('�����ҹ���Ƶ��');
legend('alpha=0','alpha=0.5','alpha=1');
figure(2);
plot(t,xt(1,:),'b',t,xt(2,:),'r',t,xt(3,:),'k');
axis([-10 10 -0.5 1.1]);xlabel('t');ylabel('�����ҹ�������');
legend('alpha=0','alpha=0.5','alpha=1');










# TODO:
# - change Emerald_Mine_Club level file's extension to proper one and create
#   score files for each level
#
Summary:	Levels for Rocks'n'Diamonds game
Summary(pl.UTF-8):	Poziomy do gry Rocks'n'Diamonds
Name:		rocksndiamonds-levels
# date of latest modification of any source
Version:	20100610
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
# extracted from http://www.artsoft.org/RELEASES/unix/rocksndiamonds/rocksndiamonds-3.0.8.tar.gz
Source0:	rocksndiamonds-3.0.8-Boulderdash.tar.gz
# Source0-md5:	d05d38c64c6e65a913932f587e37db4a
Source1:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-dx-1.0.tar.gz
# Source1-md5:	fbc250f7995c666c1c745dbaf591ce32
# http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-emc-1.0.tar.gz is obsoleted by rocksndiamonds/levels/Emerald_Mine_Club-*.7z
Source2:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-sp-1.0.tar.gz
# Source2-md5:	3af9a97e59f29995f3f7fc4da0595af6
Source3:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/BD2K3-1.0.0.zip
# Source3-md5:	ebc8e019fa9a799757d90828e242c206
Source4:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Boulder_Dash_Dream-1.0.0.zip
# Source4-md5:	a7d78a41eb13932efce568cedc9b3388
Source5:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Contributions-1.2.0.7z
# Source5-md5:	241114637643024fd427d1bf40b82e47
Source6:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Emerald_Mine_Club-2.1.1.7z
# Source6-md5:	11437b4a7a2731449dcd3aff50fa7737
Source7:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Snake_Bite-1.0.0.zip
# Source7-md5:	52ef211765c995ea40ecb646345fdc2b
Source8:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Sokoban-1.0.0.7z
# Source8-md5:	2d34a14fbee9f62a8d8bec9fdb333ec6
Source9:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Zelda-1.0.0.zip
# Source9-md5:	8e9d7c8e9d7595ac987d879774c488cd
Source10:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/ZeldaII-1.0.0.zip
# Source10-md5:	d8e6449f6ad5e29a07354e0e15290481
# rnd-contrib-1.0.0.tar.gz is obsoleted by Contributions-1.2.0.7z
URL:		http://www.artsoft.org/rocksndiamonds/levels.html
BuildRequires:	p7zip
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		rnd_rodir	%{_datadir}/games/rocksndiamonds
%define		rnd_rwdir	/var/games/rocksndiamonds

%description
Rocks'n'Diamonds is an arcade game for Unix, Mac OS X, Windows and DOS
in the tradition of:
- "Boulderdash" (8-bit),
- "Emerald Mine" (Amiga)
- "Supaplex" (Amiga/PC)
- "Sokoban" (PC)

This package contains additional levels for Rocks'n'Diamonds.

%description -l pl
Rocks'n'Diamonds to gra dla Uniksa, Mac OS X, Windows oraz DOS-a
utrzymana w tradycji gier:
- Boulderdash (ośmiobitowce),
- Emerald Mine (Amiga),
- Supaplex (Amiga/PC),
- Sokoban (PC).

Ten pakiet zawiera dodatkowe poziomy dla Rocks'n'Diamonds.

%package bd2k3
Summary:	BD2K3 level set for Rocks'n'Diamonds
Summary(pl.UTF-8):	Zestaw poziomów BD2K3 dla gry Rocks'n'Diamonds
Group:		X11/Applications/Games
Requires:	rocksndiamonds >= 3

%description bd2k3
BD2K3 level set by Alan Bond.

%description bd2k3 -l pl.UTF-8
Zestaw poziomów BD2K3 autorstwa Alana Bonda.

%package boulderdash
Summary:	Levels from several Boulderdash clones for Rocks'n'Diamonds
Summary(pl.UTF-8):	Poziomy z kilku klonów Boulderdasha dla gry Rocks'n'Diamonds
Group:		X11/Applications/Games
Requires:	rocksndiamonds >= 3

%description boulderdash
Levels from several Boulderdash clones (Boulderdash II, Boulderdash
16, xbd) taken from Rocks'n'Diamonds 3.0.8.

%description boulderdash -l pl.UTF-8
Poziomy z kilku klonów Boulderdasha (Boulderdash II, Boulderdash 16,
xbd) wzięte z Rocks'n'Diamonds 3.0.8.

%package boulderdashdream
Summary:	Boulder Dash Dream level set for Rocks'n'Diamonds
Summary(pl.UTF-8):	Zestaw poziomów Boulder Dash Dream dla gry Rocks'n'Diamonds
Group:		X11/Applications/Games
Requires:	rocksndiamonds >= 3

%description boulderdashdream
Boulder Dash Dream level set by Martijn Mooij.

%description boulderdashdream -l pl.UTF-8
Zestaw poziomów Boulder Dash Dream autorstwa Martijna Mooija.

%package contrib
Summary:	Rocks'n'Diamonds levels contributed by other players in 1995-2006
Summary(pl.UTF-8):	Poziomy do Rocks'n'Diamonds nadesłane przez innych graczy w latach 1995-2006
Group:		X11/Applications/Games
Requires:	rocksndiamonds >= 3

%description contrib
2712 Rocks'n'Diamonds levels contributed by other players in
1995-2006.

%description contrib -l pl.UTF-8
2721 poziomów do Rocks'n'Diamonds nadesłanych przez innych graczy w
latach 1995-2006.

%package dx
Summary:	Levels from DX Boulderdash for Rocks'n'Diamonds
Summary(pl.UTF-8):	Poziomy z DX Boulderdash dla gry Rocks'n'Diamonds
Group:		X11/Applications/Games
Requires:	rocksndiamonds >= 3

%description dx
1400 levels from DX Boulderdash.

%description dx -l pl.UTF-8
1400 poziomów z DX Boulderdash.

%package emc
Summary:	Levels from Emerald Mine Club for Rocks'n'Diamonds
Summary(pl.UTF-8):	Poziomy z Klubu Emerald Mine dla gry Rocks'n'Diamonds
Group:		X11/Applications/Games
Requires:	rocksndiamonds >= 3

%description emc
10318 levels from Emerald Mine Club.

%description emc -l pl.UTF-8
10318 poziomów z Klubu Emerald Mine.

%package snakebite
Summary:	Snake Bite levels for Rocks'n'Diamonds
Summary(pl.UTF-8):	Poziomy Snake Bite dla gry Rocks'n'Diamonds
Group:		X11/Applications/Games
Requires:	rocksndiamonds >= 3

%description snakebite
Snake Bite levels.

%description snakebite -l pl.UTF-8
Poziomy Snake Bite.

%package sokoban
Summary:	Sokoban style levels for Rocks'n'Diamonds
Summary(pl.UTF-8):	Poziomy w stylu Sokobana dla gry Rocks'n'Diamonds
Group:		X11/Applications/Games
Requires:	rocksndiamonds >= 3

%description sokoban
764 Sokoban style levels.

%description sokoban -l pl.UTF-8
764 poziomy w stylu Sokobana.

%package supaplex
Summary:	Supaplex style levels for Rocks'n'Diamonds
Summary(pl.UTF-8):	Poziomy w stylu Supapleksa dla gry Rocks'n'Diamonds
Group:		X11/Applications/Games
Requires:	rocksndiamonds >= 3

%description supaplex
1443 Supaplex style levels.

%description supaplex -l pl.UTF-8
1443 poziomy w stylu Supaplexa.

%package zelda
Summary:	Zelda levels for Rocks'n'Diamonds
Summary(pl.UTF-8):	Poziomy Zelda dla gry Rocks'n'Diamonds
Group:		X11/Applications/Games
Requires:	rocksndiamonds >= 3

%description zelda
2 levels: Zelda and Zelda 2.

%description zelda -l pl.UTF-8
2 poziomy: Zelda oraz Zelda 2.

%prep
%setup -q -c -a1 -a2
unzip -q %{SOURCE3} -d levels
unzip -q %{SOURCE4} -d levels
7z x %{SOURCE5} -olevels
7z x %{SOURCE6} -olevels
unzip -q %{SOURCE7} -d levels
7z x %{SOURCE8} -olevels
unzip -q %{SOURCE9} -d levels
unzip -q %{SOURCE10} -d levels

%install
install -d $RPM_BUILD_ROOT{%{rnd_rodir},%{rnd_rwdir}}

cp -a levels $RPM_BUILD_ROOT%{rnd_rodir}

# scores
install -d $RPM_BUILD_ROOT%{rnd_rwdir}/scores
cd $RPM_BUILD_ROOT%{rnd_rodir}/levels
set +x
for i in *; do
	echo "Preparing score file for $i"
	cd $i
	for file in `find . -name '*.level' -type f`; do
		dir=$(dirname "$file")
		if [ "$dir" = "." ]; then
			dir="$i"
		fi
		file=$(basename "$file" .level)
		install -d $RPM_BUILD_ROOT%{rnd_rwdir}/scores/${dir}
		touch $RPM_BUILD_ROOT%{rnd_rwdir}/scores/${dir}/${file}.score
		echo -n .
	done
	cd ..
	echo "OK"
done
set -x
%{__rm} $RPM_BUILD_ROOT%{rnd_rodir}/levels/BD2K3/readme.txt
%{__rm} $RPM_BUILD_ROOT%{rnd_rodir}/levels/Boulder_Dash_Dream/readme.txt
%{__rm} $RPM_BUILD_ROOT%{rnd_rodir}/levels/zelda/readme.txt
#remove titlemessage_1.txt too?
%{__rm} $RPM_BUILD_ROOT%{rnd_rodir}/levels/zelda2/readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files bd2k3
%defattr(644,root,root,755)
%doc levels/BD2K3/readme.txt
%{rnd_rodir}/levels/BD2K3
%defattr(664,root,games,755)
%dir %{rnd_rwdir}/scores/BD2K3
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/BD2K3/*.score

%files boulderdash
%defattr(644,root,root,755)
%{rnd_rodir}/levels/Boulderdash
%defattr(664,root,games,755)
%dir %{rnd_rwdir}/scores/bd_boulderdash_2
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/bd_boulderdash_2/*.score
%dir %{rnd_rwdir}/scores/bd_boulderdash_16
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/bd_boulderdash_16/*.score
%dir %{rnd_rwdir}/scores/bd_xbd
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/bd_xbd/*.score

%files boulderdashdream
%defattr(644,root,root,755)
%{rnd_rodir}/levels/Boulder_Dash_Dream
%defattr(664,root,games,755)
%dir %{rnd_rwdir}/scores/Boulder_Dash_Dream
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Boulder_Dash_Dream/*.score

%files contrib
%defattr(644,root,root,755)
%{rnd_rodir}/levels/Contributions
%defattr(664,root,games,755)
%dir %{rnd_rwdir}/scores/Contributions_1995
%dir %{rnd_rwdir}/scores/Contributions_1995/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_1995/rnd_*/*.score
%dir %{rnd_rwdir}/scores/Contributions_1996
%dir %{rnd_rwdir}/scores/Contributions_1996/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_1996/rnd_*/*.score
%dir %{rnd_rwdir}/scores/Contributions_1997
%dir %{rnd_rwdir}/scores/Contributions_1997/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_1997/rnd_*/*.score
%dir %{rnd_rwdir}/scores/Contributions_1998
%dir %{rnd_rwdir}/scores/Contributions_1998/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_1998/rnd_*/*.score
%dir %{rnd_rwdir}/scores/Contributions_1999
%dir %{rnd_rwdir}/scores/Contributions_1999/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_1999/rnd_*/*.score
%dir %{rnd_rwdir}/scores/Contributions_2000
%dir %{rnd_rwdir}/scores/Contributions_2000/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_2000/rnd_*/*.score
%dir %{rnd_rwdir}/scores/Contributions_2001
%dir %{rnd_rwdir}/scores/Contributions_2001/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_2001/rnd_*/*.score
%dir %{rnd_rwdir}/scores/Contributions_2002
%dir %{rnd_rwdir}/scores/Contributions_2002/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_2002/rnd_*/*.score
%dir %{rnd_rwdir}/scores/Contributions_2003
%dir %{rnd_rwdir}/scores/Contributions_2003/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_2003/rnd_*/*.score
%dir %{rnd_rwdir}/scores/Contributions_2004
%dir %{rnd_rwdir}/scores/Contributions_2004/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_2004/rnd_*/*.score
%dir %{rnd_rwdir}/scores/Contributions_2005
%dir %{rnd_rwdir}/scores/Contributions_2005/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_2005/rnd_*/*.score
%dir %{rnd_rwdir}/scores/Contributions_2006
%dir %{rnd_rwdir}/scores/Contributions_2006/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/Contributions_2006/rnd_*/*.score
# FIXME: to base?
#%dir %{rnd_rwdir}/scores/rnd_*
#%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/rnd_*/*.score

%files dx
%defattr(644,root,root,755)
%{rnd_rodir}/levels/DX_Boulderdash
%defattr(664,root,games,755)
%dir %{rnd_rwdir}/scores/dx_abd
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_abd/*.score
%dir %{rnd_rwdir}/scores/dx_achim_haertel
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_achim_haertel/*.score
%dir %{rnd_rwdir}/scores/dx_bd4
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_bd4/*.score
%dir %{rnd_rwdir}/scores/dx_blunderdash
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_blunderdash/*.score
%dir %{rnd_rwdir}/scores/dx_boulderdash5
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_boulderdash5/*.score
%dir %{rnd_rwdir}/scores/dx_dc2classic
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_dc2classic/*.score
%dir %{rnd_rwdir}/scores/dx_firefox1
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_firefox1/*.score
%dir %{rnd_rwdir}/scores/dx_forgottenmine1
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_forgottenmine1/*.score
%dir %{rnd_rwdir}/scores/dx_manfred_tausch
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_manfred_tausch/*.score
%dir %{rnd_rwdir}/scores/dx_martin_brentnall
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_martin_brentnall/*.score
%dir %{rnd_rwdir}/scores/dx_no_one_1-3
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_no_one_1-3/*.score
%dir %{rnd_rwdir}/scores/dx_no_one_4-6
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_no_one_4-6/*.score
%dir %{rnd_rwdir}/scores/dx_peter_broadribb
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_peter_broadribb/*.score
%dir %{rnd_rwdir}/scores/dx_tutorial
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/dx_tutorial/*.score

%files emc
%defattr(644,root,root,755)
%{rnd_rodir}/levels/Emerald_Mine_Club
%defattr(664,root,games,755)
#%%dir %{rnd_rwdir}/scores/emc*
#%%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/emc*/*.score

%files snakebite
%defattr(644,root,root,755)
%{rnd_rodir}/levels/Snake_Bite
%defattr(664,root,games,755)
%dir %{rnd_rwdir}/scores/snake_bite
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/snake_bite/*.score
%dir %{rnd_rwdir}/scores/snake_bite_jue
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/snake_bite_jue/*.score

%files sokoban
%defattr(644,root,root,755)
%{rnd_rodir}/levels/Sokoban
%defattr(664,root,games,755)
%dir %{rnd_rwdir}/scores/sb_mas_sasquatch
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/sb_mas_sasquatch/*.score
%dir %{rnd_rwdir}/scores/sb_microban
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/sb_microban/*.score
%dir %{rnd_rwdir}/scores/sb_sasquatch_1
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/sb_sasquatch_1/*.score
%dir %{rnd_rwdir}/scores/sb_sasquatch_3
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/sb_sasquatch_3/*.score
%dir %{rnd_rwdir}/scores/sb_sasquatch_4
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/sb_sasquatch_4/*.score
%dir %{rnd_rwdir}/scores/sb_sokomania_spaceship_1
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/sb_sokomania_spaceship_1/*.score
%dir %{rnd_rwdir}/scores/sb_sokomania_spaceship_2
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/sb_sokomania_spaceship_2/*.score

%files supaplex
%defattr(644,root,root,755)
%{rnd_rodir}/levels/Supaplex
%defattr(664,root,games,755)
%dir %{rnd_rwdir}/scores/supaplex_01
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_01/*.score
%dir %{rnd_rwdir}/scores/supaplex_02
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_02/*.score
%dir %{rnd_rwdir}/scores/supaplex_03
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_03/*.score
%dir %{rnd_rwdir}/scores/supaplex_04
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_04/*.score
%dir %{rnd_rwdir}/scores/supaplex_05
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_05/*.score
%dir %{rnd_rwdir}/scores/supaplex_06
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_06/*.score
%dir %{rnd_rwdir}/scores/supaplex_07
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_07/*.score
%dir %{rnd_rwdir}/scores/supaplex_08
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_08/*.score
%dir %{rnd_rwdir}/scores/supaplex_95
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_95/*.score
%dir %{rnd_rwdir}/scores/supaplex_96
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_96/*.score
%dir %{rnd_rwdir}/scores/supaplex_97
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_97/*.score
%dir %{rnd_rwdir}/scores/supaplex_98
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_98/*.score
%dir %{rnd_rwdir}/scores/supaplex_99
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/supaplex_99/*.score

%files zelda
%defattr(644,root,root,755)
%{rnd_rodir}/levels/zelda
%{rnd_rodir}/levels/zelda2
%defattr(664,root,games,755)
%dir %{rnd_rwdir}/scores/zelda
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/zelda/*.score
%dir %{rnd_rwdir}/scores/zelda2
%config(noreplace) %verify(not md5 mtime size) %{rnd_rwdir}/scores/zelda2/*.score

# -*- coding: utf-8 -*-
# ·


class BlkDevData(object):
    def __init__(self, data):

        super().__init__()

        self.properties = self.all_properties

        if isinstance(data, dict) or isinstance(data, BlkDevData):
            _dev = data
        else:
            raise ValueError(
                "Los datos no corresponden a un dispositivo de bloques")

        for _prop in self.properties:
            self[_prop] = _dev[_prop]

        if self.__type == "disk":
            self.__properties = self.dev_properties
        elif self.__type == "part":
            self.__properties = self.part_properties
        elif self.__type == "crypt":
            self.__properties = self.vol_properties

    def __getitem__(self, item):
        if item == "name":
            return self.name
        if item == "kname":
            return self.kname
        if item == "path":
            return self.path
        if item == "maj:min":
            return self.maj_min
        if item == "fsavail":
            return self.fsavail
        if item == "fssize":
            return self.fssize
        if item == "fstype":
            return self.fstype
        if item == "fsused":
            return self.fsused
        if item == "fsuse%":
            return self.fsuse
        if item == "mountpoint":
            return self.mountpoint
        if item == "label":
            return self.label
        if item == "uuid":
            return self.uuid
        if item == "ptuuid":
            return self.ptuuid
        if item == "pttype":
            return self.pttype
        if item == "parttype":
            return self.parttype
        if item == "partlabel":
            return self.partlabel
        if item == "partuuid":
            return self.partuuid
        if item == "partflags":
            return self.partflags
        if item == "ra":
            return self.ra
        if item == "ro":
            return self.ro
        if item == "rm":
            return self.rm
        if item == "hotplug":
            return self.hotplug
        if item == "model":
            return self.model
        if item == "serial":
            return self.serial
        if item == "size":
            return self.size
        if item == "state":
            return self.state
        if item == "owner":
            return self.owner
        if item == "group":
            return self.group
        if item == "mode":
            return self.mode
        if item == "alignment":
            return self.alignment
        if item == "min-io":
            return self.min_io
        if item == "opt-io":
            return self.opt_io
        if item == "phy-sec":
            return self.phy_sec
        if item == "log-sec":
            return self.log_sec
        if item == "rota":
            return self.rota
        if item == "sched":
            return self.sched
        if item == "rq-size":
            return self.rq_size
        if item == "type":
            return self.type
        if item == "disc-aln":
            return self.disc_aln
        if item == "disc-gran":
            return self.disc_gran
        if item == "disc-max":
            return self.disc_max
        if item == "disc-zero":
            return self.disc_zero
        if item == "wsame":
            return self.wsame
        if item == "wwn":
            return self.wwn
        if item == "rand":
            return self.rand
        if item == "pkname":
            return self.pkname
        if item == "hctl":
            return self.hctl
        if item == "tran":
            return self.tran
        if item == "subsystems":
            return self.subsystems
        if item == "rev":
            return self.rev
        if item == "vendor":
            return self.vendor
        if item == "zoned":
            return self.zoned
        return None

    def __setitem__(self, item, value):
        if item == "name":
            self.name = value
            return
        if item == "kname":
            self.kname = value
            return
        if item == "path":
            self.path = value
            return
        if item == "maj:min":
            self.maj_min = value
            return
        if item == "fsavail":
            self.fsavail = value
            return
        if item == "fssize":
            self.fssize = value
            return
        if item == "fstype":
            self.fstype = value
            return
        if item == "fsused":
            self.fsused = value
            return
        if item == "fsuse%":
            self.fsuse = value
            return
        if item == "mountpoint":
            self.mountpoint = value
            return
        if item == "label":
            self.label = value
            return
        if item == "uuid":
            self.uuid = value
            return
        if item == "ptuuid":
            self.ptuuid = value
            return
        if item == "pttype":
            self.pttype = value
            return
        if item == "parttype":
            self.parttype = value
            return
        if item == "partlabel":
            self.partlabel = value
            return
        if item == "partuuid":
            self.partuuid = value
            return
        if item == "partflags":
            self.partflags = value
            return
        if item == "ra":
            self.ra = value
            return
        if item == "ro":
            self.ro = value
            return
        if item == "rm":
            self.rm = value
            return
        if item == "hotplug":
            self.hotplug = value
            return
        if item == "model":
            self.model = value
            return
        if item == "serial":
            self.serial = value
            return
        if item == "size":
            self.size = value
            return
        if item == "state":
            self.state = value
            return
        if item == "owner":
            self.owner = value
            return
        if item == "group":
            self.group = value
            return
        if item == "mode":
            self.mode = value
            return
        if item == "alignment":
            self.alignment = value
            return
        if item == "min-io":
            self.min_io = value
            return
        if item == "opt-io":
            self.opt_io = value
            return
        if item == "phy-sec":
            self.phy_sec = value
            return
        if item == "log-sec":
            self.log_sec = value
            return
        if item == "rota":
            self.rota = value
            return
        if item == "sched":
            self.sched = value
            return
        if item == "rq-size":
            self.rq_size = value
            return
        if item == "type":
            self.type = value
            return
        if item == "disc-aln":
            self.disc_aln = value
            return
        if item == "disc-gran":
            self.disc_gran = value
            return
        if item == "disc-max":
            self.disc_max = value
            return
        if item == "disc-zero":
            self.disc_zero = value
            return
        if item == "wsame":
            self.wsame = value
            return
        if item == "wwn":
            self.wwn = value
            return
        if item == "rand":
            self.rand = value
            return
        if item == "pkname":
            self.pkname = value
            return
        if item == "hctl":
            self.hctl = value
            return
        if item == "tran":
            self.tran = value
            return
        if item == "subsystems":
            self.subsystems = value
            return
        if item == "rev":
            self.rev = value
            return
        if item == "vendor":
            self.vendor = value
            return
        if item == "zoned":
            self.zoned = value
            return

    def __len__(self):
        lenOfData = 0
        for prop in self.__properties:
            if self[prop] is not None:
                lenOfData += 1
        return lenOfData

    @property
    def all_properties(self):
        return [
            "name", "kname", "path", "maj:min", "fsavail", "fssize", "fstype",
            "fsused", "fsuse%", "mountpoint", "label", "uuid", "ptuuid",
            "pttype", "parttype", "partlabel", "partuuid", "partflags", "ra",
            "ro", "rm", "hotplug", "model", "serial", "size", "state", "owner",
            "group", "mode", "alignment", "min-io", "opt-io", "phy-sec",
            "log-sec", "rota", "sched", "rq-size", "type", "disc-aln",
            "disc-gran", "disc-max", "disc-zero", "wsame", "wwn", "rand",
            "pkname", "hctl", "tran", "subsystems", "rev", "vendor", "zoned"
        ]

    @property
    def dev_properties(self):
        return [
            "name", "kname", "path", "maj:min", "fsavail", "fssize", "fstype",
            "fsused", "fsuse%", "mountpoint", "ptuuid", "pttype", "ra", "ro",
            "rm", "hotplug", "model", "serial", "size", "state", "mode",
            "alignment", "min-io", "opt-io", "phy-sec", "log-sec", "rota",
            "sched", "rq-size", "type", "disc-aln", "disc-gran", "disc-max",
            "disc-zero", "wsame", "wwn", "rand", "hctl", "tran", "subsystems",
            "rev", "vendor", "zoned"
        ]

    @property
    def part_properties(self):
        return [
            "name", "kname", "path", "maj:min", "fsavail", "fssize", "fstype",
            "fsused", "fsuse%", "mountpoint", "label", "uuid", "parttype",
            "partuuid", "ra", "ro", "rm", "hotplug", "model", "serial", "size",
            "mode", "alignment", "min-io", "opt-io", "phy-sec", "log-sec",
            "rota", "sched", "rq-size", "type", "disc-aln", "disc-gran",
            "disc-max", "disc-zero", "wsame", "rand", "pkname", "subsystems",
            "zoned"
        ]

    @property
    def vol_properties(self):
        return [
            "name", "kname", "path", "maj:min", "fsavail", "fssize", "fstype",
            "fsused", "fsuse%", "mountpoint", "label", "uuid", "ra", "ro",
            "rm", "hotplug", "size", "state", "mode", "alignment", "min-io",
            "opt-io", "phy-sec", "log-sec", "rota", "rq-size", "type",
            "disc-aln", "disc-gran", "disc-max", "disc-zero", "wsame", "rand",
            "pkname", "subsystems", "zoned"
        ]

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, props):
        if not isinstance(props, list):
            return
        for prop in props:
            if prop not in self.all_properties:
                return
        self.__properties = props

    def keys(self):
        return self.__properties

    # -----------------------------------------------

    @property
    def name(self):
        return self.__name

    @property
    def kname(self):
        return self.__kname

    @property
    def path(self):
        return self.__path

    @property
    def maj_min(self):
        return self.__maj_min

    @property
    def fsavail(self):
        return self.__fsavail

    @property
    def fssize(self):
        return self.__fssize

    @property
    def fstype(self):
        return self.__fstype

    @property
    def fsused(self):
        return self.__fsused

    @property
    def fsuse(self):
        return self.__fsuse

    @property
    def mountpoint(self):
        return self.__mountpoint

    @property
    def label(self):
        return self.__label

    @property
    def uuid(self):
        return self.__uuid

    @property
    def ptuuid(self):
        return self.__ptuuid

    @property
    def pttype(self):
        return self.__pttype

    @property
    def parttype(self):
        return self.__parttype

    @property
    def partlabel(self):
        return self.__partlabel

    @property
    def partuuid(self):
        return self.__partuuid

    @property
    def partflags(self):
        return self.__partflags

    @property
    def ra(self):
        return self.__ra

    @property
    def ro(self):
        return self.__ro

    @property
    def rm(self):
        return self.__rm

    @property
    def hotplug(self):
        return self.__hotplug

    @property
    def model(self):
        return self.__model

    @property
    def serial(self):
        return self.__serial

    @property
    def size(self):
        return self.__size

    @property
    def state(self):
        return self.__state

    @property
    def owner(self):
        return self.__owner

    @property
    def group(self):
        return self.__group

    @property
    def mode(self):
        return self.__mode

    @property
    def alignment(self):
        return self.__alignment

    @property
    def min_io(self):
        return self.__min_io

    @property
    def opt_io(self):
        return self.__opt_io

    @property
    def phy_sec(self):
        return self.__phy_sec

    @property
    def log_sec(self):
        return self.__log_sec

    @property
    def rota(self):
        return self.__rota

    @property
    def sched(self):
        return self.__sched

    @property
    def rq_size(self):
        return self.__rq_size

    @property
    def type(self):
        return self.__type

    @property
    def disc_aln(self):
        return self.__disc_aln

    @property
    def disc_gran(self):
        return self.__disc_gran

    @property
    def disc_max(self):
        return self.__disc_max

    @property
    def disc_zero(self):
        return self.__disc_zero

    @property
    def wsame(self):
        return self.__wsame

    @property
    def wwn(self):
        return self.__wwn

    @property
    def rand(self):
        return self.__rand

    @property
    def pkname(self):
        return self.__pkname

    @property
    def hctl(self):
        return self.__hctl

    @property
    def tran(self):
        return self.__tran

    @property
    def subsystems(self):
        return self.__subsystems

    @property
    def rev(self):
        return self.__rev

    @property
    def vendor(self):
        return self.__vendor

    @property
    def zoned(self):
        return self.__zoned

    # ---------------------------------------

    @name.setter
    def name(self, value):
        self.__name = value

    @kname.setter
    def kname(self, value):
        self.__kname = value

    @path.setter
    def path(self, value):
        self.__path = value

    @maj_min.setter
    def maj_min(self, value):
        self.__maj_min = value

    @fsavail.setter
    def fsavail(self, value):
        self.__fsavail = value

    @fssize.setter
    def fssize(self, value):
        self.__fssize = value

    @fstype.setter
    def fstype(self, value):
        self.__fstype = value

    @fsused.setter
    def fsused(self, value):
        self.__fsused = value

    @fsuse.setter
    def fsuse(self, value):
        self.__fsuse = value

    @mountpoint.setter
    def mountpoint(self, value):
        self.__mountpoint = value

    @label.setter
    def label(self, value):
        self.__label = value

    @uuid.setter
    def uuid(self, value):
        self.__uuid = value

    @ptuuid.setter
    def ptuuid(self, value):
        self.__ptuuid = value

    @pttype.setter
    def pttype(self, value):
        self.__pttype = value

    @parttype.setter
    def parttype(self, value):
        self.__parttype = value

    @partlabel.setter
    def partlabel(self, value):
        self.__partlabel = value

    @partuuid.setter
    def partuuid(self, value):
        self.__partuuid = value

    @partflags.setter
    def partflags(self, value):
        self.__partflags = value

    @ra.setter
    def ra(self, value):
        self.__ra = value

    @ro.setter
    def ro(self, value):
        self.__ro = value

    @rm.setter
    def rm(self, value):
        self.__rm = value

    @hotplug.setter
    def hotplug(self, value):
        self.__hotplug = value

    @model.setter
    def model(self, value):
        self.__model = value

    @serial.setter
    def serial(self, value):
        self.__serial = value

    @size.setter
    def size(self, value):
        self.__size = value

    @state.setter
    def state(self, value):
        self.__state = value

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @group.setter
    def group(self, value):
        self.__group = value

    @mode.setter
    def mode(self, value):
        self.__mode = value

    @alignment.setter
    def alignment(self, value):
        self.__alignment = value

    @min_io.setter
    def min_io(self, value):
        self.__min_io = value

    @opt_io.setter
    def opt_io(self, value):
        self.__opt_io = value

    @phy_sec.setter
    def phy_sec(self, value):
        self.__phy_sec = value

    @log_sec.setter
    def log_sec(self, value):
        self.__log_sec = value

    @rota.setter
    def rota(self, value):
        self.__rota = value

    @sched.setter
    def sched(self, value):
        self.__sched = value

    @rq_size.setter
    def rq_size(self, value):
        self.__rq_size = value

    @type.setter
    def type(self, value):
        self.__type = value

    @disc_aln.setter
    def disc_aln(self, value):
        self.__disc_aln = value

    @disc_gran.setter
    def disc_gran(self, value):
        self.__disc_gran = value

    @disc_max.setter
    def disc_max(self, value):
        self.__disc_max = value

    @disc_zero.setter
    def disc_zero(self, value):
        self.__disc_zero = value

    @wsame.setter
    def wsame(self, value):
        self.__wsame = value

    @wwn.setter
    def wwn(self, value):
        self.__wwn = value

    @rand.setter
    def rand(self, value):
        self.__rand = value

    @pkname.setter
    def pkname(self, value):
        self.__pkname = value

    @hctl.setter
    def hctl(self, value):
        self.__hctl = value

    @tran.setter
    def tran(self, value):
        self.__tran = value

    @subsystems.setter
    def subsystems(self, value):
        self.__subsystems = value

    @rev.setter
    def rev(self, value):
        self.__rev = value

    @vendor.setter
    def vendor(self, value):
        self.__vendor = value

    @zoned.setter
    def zoned(self, value):
        self.__zoned = value

    # -----------------------------------------------

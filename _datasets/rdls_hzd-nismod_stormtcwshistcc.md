---
attributions:
- entity:
    affiliation: null
    email: info@deltares.nl
    name: Deltares, Delft, The Netherlands
    url: https://www.deltares.nl/en
  id: attribution_collaborator_1
  role: collaborator
- entity:
    affiliation: null
    email: pers@knmi.nl
    name: Royal Netherlands Meteorological Institute (KNMI), De Bilt, The Netherlands
    url: https://www.knmi.nl/over-het-knmi/about
  id: attribution_collaborator_2
  role: collaborator
- entity:
    affiliation: null
    email: enquiries@bodc.ac.uk
    name: University of Southampton, National Oceanography Centre, School of Ocean
      and Earth Science
    url: https://noc.ac.uk/
  id: attribution_collaborator_3
  role: collaborator
- entity:
    affiliation: null
    email: info.ivm@vu.nl
    name: Vrije Universiteit Amsterdam, Institute for Environmental Studies (IVM)
    url: https://vu.nl/en/about-vu/research-institutes/ivm
  id: attribution_collaborator_4
  role: collaborator
- entity:
    affiliation: null
    email: angela.wenham@economics.ox.ac.uk
    name: Climate Econometrics, Nuffield College, Oxford, UK
    url: https://www.nuffield.ox.ac.uk/our-research/research-centres/climate-econometrics/
  id: attribution_collaborator_5
  role: collaborator
- entity:
    affiliation: null
    email: enquiries@metoffice.gov.uk
    name: MetOffice, Exeter, UK
    url: https://www.metoffice.gov.uk/
  id: attribution_collaborator_6
  role: collaborator
- entity:
    affiliation: null
    email: OEP@treasury.gov
    name: Office of Macroeconomic Analysis, U.S. Department of the Treasury
    url: https://home.treasury.gov/about/offices/economic-policy
  id: attribution_collaborator_7
  role: collaborator
catalog: null
contact_point:
  affiliation: null
  email: nadia.bloemendaal@vu.nl
  name: Nadia Bloemendaal
  url: https://vu.nl/en/about-vu/research-institutes/ivm
creator:
  affiliation: null
  email: nadia.bloemendaal@vu.nl
  name: Nadia Bloemendaal
  url: https://vu.nl/en/about-vu/research-institutes/ivm
dataset_id: rdls_hzd-nismod_stormtcwshistcc
description: Gridded and table-based tropical-cyclone wind-hazard datasets providing
  maximum wind speeds at fixed return periods and return periods at fixed wind speeds
  for present climate (1980-2018) and climate change scenarios (1979-2014 baseline
  and 2015-2050 projections); gridded products are ~10 km per basin, and city/island
  tables summarize conditions within 100 km. Climate change datasets incorporate signals
  from four GCMs (CMCC-CM2-VHR4, CNRM-CM6-1-HR, EC-Earth3P-HR, HadGEM3-GC31-HM).
details: "Datasets were generated with the statistical STORM algorithm. Present climate\
  \ dataset uses IBTrACS historical tracks (1980-2018) with ERA5 monthly-mean environmental\
  \ conditions. Climate change datasets add signals from four GCMs (CMCC-CM2-VHR4,\
  \ CNRM-CM6-1-HR, EC-Earth3P-HR, HadGEM3-GC31-HM) to project future conditions. A\
  \ 2-D parametric wind model was applied to produce ~10 km fields, and return periods\
  \ (or wind speeds) were derived empirically with Weibull's plotting formula. Datasets\
  \ include, for each grid cell (or city/island entry), the mean, standard deviation,\
  \ and 5-95% confidence intervals across 1,000 realizations; basin IDs (EP, NA, NI,\
  \ SI, SP, WP) and fixed value sets for return periods (10-10,000 yr) and wind speeds\
  \ (20-75 m s\u207B\xB9 with additional threshold values) are provided."
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 44
    events:
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP10 (10-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP10
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability:
            span: 1
            value: 0.1
          return_period: 10
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP20 (20-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP20
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.05
          probability:
            span: 1
            value: 0.05
          return_period: 20
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP30 (30-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP30
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.033333
          probability:
            span: 1
            value: 0.033333
          return_period: 30
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP40 (40-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP40
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.025
          probability:
            span: 1
            value: 0.025
          return_period: 40
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP50 (50-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP50
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability:
            span: 1
            value: 0.02
          return_period: 50
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP60 (60-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP60
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.016667
          probability:
            span: 1
            value: 0.016667
          return_period: 60
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP70 (70-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP70
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.014286
          probability:
            span: 1
            value: 0.014286
          return_period: 70
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP80 (80-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP80
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.0125
          probability:
            span: 1
            value: 0.0125
          return_period: 80
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP90 (90-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP90
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.011111
          probability:
            span: 1
            value: 0.011111
          return_period: 90
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP100 (100-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP100
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability:
            span: 1
            value: 0.01
          return_period: 100
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP200 (200-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP200
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.005
          probability:
            span: 1
            value: 0.005
          return_period: 200
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP300 (300-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP300
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.003333
          probability:
            span: 1
            value: 0.003333
          return_period: 300
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP400 (400-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP400
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.0025
          probability:
            span: 1
            value: 0.0025
          return_period: 400
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP500 (500-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP500
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.002
          probability:
            span: 1
            value: 0.002
          return_period: 500
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP600 (600-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP600
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.001667
          probability:
            span: 1
            value: 0.001667
          return_period: 600
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP700 (700-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP700
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.001429
          probability:
            span: 1
            value: 0.001429
          return_period: 700
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP800 (800-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP800
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.00125
          probability:
            span: 1
            value: 0.00125
          return_period: 800
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP900 (900-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP900
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.001111
          probability:
            span: 1
            value: 0.001111
          return_period: 900
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP1000 (1000-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP1000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.001
          probability:
            span: 1
            value: 0.001
          return_period: 1000
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP2000 (2000-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP2000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.0005
          probability:
            span: 1
            value: 0.0005
          return_period: 2000
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP3000 (3000-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP3000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000333
          probability:
            span: 1
            value: 0.000333
          return_period: 3000
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP4000 (4000-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP4000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.00025
          probability:
            span: 1
            value: 0.00025
          return_period: 4000
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP5000 (5000-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP5000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.0002
          probability:
            span: 1
            value: 0.0002
          return_period: 5000
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP6000 (6000-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP6000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000167
          probability:
            span: 1
            value: 0.000167
          return_period: 6000
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP7000 (7000-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP7000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000143
          probability:
            span: 1
            value: 0.000143
          return_period: 7000
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP8000 (8000-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP8000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000125
          probability:
            span: 1
            value: 0.000125
          return_period: 8000
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP9000 (9000-year
        return period). Per-basin about 10 km grids; includes mean, standard deviation,
        and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP9000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000111
          probability:
            span: 1
            value: 0.000111
          return_period: 9000
    - calculation_method: simulated
      description: STORM fixed-return-period maximum wind speed (m/s) for RP10000
        (10000-year return period). Per-basin about 10 km grids; includes mean, standard
        deviation, and 5-95% confidence intervals over 1,000 realizations.
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS_PRESENT
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP10000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.0001
          probability:
            span: 1
            value: 0.0001
          return_period: 10000
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS18MS (18 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS18MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS20MS (20 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS20MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS25MS (25 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS25MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS30MS (30 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS30MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS33MS (33 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS33MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS35MS (35 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS35MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS40MS (40 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS40MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS42MS (42 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS42MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS45MS (45 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS45MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS50MS (50 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS50MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS55MS (55 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS55MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS58MS (58 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS58MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS60MS (60 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS60MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS65MS (65 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS65MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS70MS (70 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS70MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: Per-basin ~10 km grids of return period (years) for fixed wind
        speed WS75MS (75 m/s), from STORM fixed-wind-speed products (20-75 m/s at
        5 m/s steps, plus 18, 33, 42, 58 m/s).
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS75MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: STORM_FIXED_RETURN_PERIODS_PRESENT
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    - classification: null
      id: STORM_FIXED_WIND_SPEEDS
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    - classification: null
      id: STORM_CITIES_TC_WIND_SPEED_RETURN_PERIODS
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    - classification: null
      id: STORM_ISLANDS_TC_WIND_SPEED_RETURN_PERIODS
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_storm_tropical_cyclone
    occurrence_range: 1/10 to 1/10000 years
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 44
    events:
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP10
        (10-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP10
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability:
            span: 1
            value: 0.1
          return_period: 10
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP20
        (20-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP20
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.05
          probability:
            span: 1
            value: 0.05
          return_period: 20
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP30
        (30-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP30
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.033333
          probability:
            span: 1
            value: 0.033333
          return_period: 30
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP40
        (40-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP40
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.025
          probability:
            span: 1
            value: 0.025
          return_period: 40
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP50
        (50-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP50
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability:
            span: 1
            value: 0.02
          return_period: 50
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP60
        (60-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP60
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.016667
          probability:
            span: 1
            value: 0.016667
          return_period: 60
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP70
        (70-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP70
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.014286
          probability:
            span: 1
            value: 0.014286
          return_period: 70
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP80
        (80-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP80
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.0125
          probability:
            span: 1
            value: 0.0125
          return_period: 80
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP90
        (90-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP90
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.011111
          probability:
            span: 1
            value: 0.011111
          return_period: 90
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP100
        (100-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP100
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability:
            span: 1
            value: 0.01
          return_period: 100
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP200
        (200-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP200
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.005
          probability:
            span: 1
            value: 0.005
          return_period: 200
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP300
        (300-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP300
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.003333
          probability:
            span: 1
            value: 0.003333
          return_period: 300
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP400
        (400-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP400
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.0025
          probability:
            span: 1
            value: 0.0025
          return_period: 400
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP500
        (500-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP500
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.002
          probability:
            span: 1
            value: 0.002
          return_period: 500
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP600
        (600-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP600
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.001667
          probability:
            span: 1
            value: 0.001667
          return_period: 600
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP700
        (700-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP700
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.001429
          probability:
            span: 1
            value: 0.001429
          return_period: 700
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP800
        (800-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP800
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.00125
          probability:
            span: 1
            value: 0.00125
          return_period: 800
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP900
        (900-year return period) on ~10 km grids for all ocean basins (available as
        GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP900
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.001111
          probability:
            span: 1
            value: 0.001111
          return_period: 900
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP1000
        (1,000-year return period) on ~10 km grids for all ocean basins (available
        as GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP1000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.001
          probability:
            span: 1
            value: 0.001
          return_period: 1000
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP2000
        (2,000-year return period) on ~10 km grids for all ocean basins (available
        as GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP2000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.0005
          probability:
            span: 1
            value: 0.0005
          return_period: 2000
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP3000
        (3,000-year return period) on ~10 km grids for all ocean basins (available
        as GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP3000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000333
          probability:
            span: 1
            value: 0.000333
          return_period: 3000
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP4000
        (4,000-year return period) on ~10 km grids for all ocean basins (available
        as GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP4000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.00025
          probability:
            span: 1
            value: 0.00025
          return_period: 4000
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP5000
        (5,000-year return period) on ~10 km grids for all ocean basins (available
        as GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP5000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.0002
          probability:
            span: 1
            value: 0.0002
          return_period: 5000
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP6000
        (6,000-year return period) on ~10 km grids for all ocean basins (available
        as GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP6000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000167
          probability:
            span: 1
            value: 0.000167
          return_period: 6000
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP7000
        (7,000-year return period) on ~10 km grids for all ocean basins (available
        as GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP7000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000143
          probability:
            span: 1
            value: 0.000143
          return_period: 7000
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP8000
        (8,000-year return period) on ~10 km grids for all ocean basins (available
        as GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP8000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000125
          probability:
            span: 1
            value: 0.000125
          return_period: 8000
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP9000
        (9,000-year return period) on ~10 km grids for all ocean basins (available
        as GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP9000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000111
          probability:
            span: 1
            value: 0.000111
          return_period: 9000
    - calculation_method: simulated
      description: 'STORM Fixed Return Periods: maximum wind speed (m/s) for RP10000
        (10,000-year return period) on ~10 km grids for all ocean basins (available
        as GeoTIFF tiles and gridded NetCDF variants, including multi-model and MEDIAN
        products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_RETURN_PERIODS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: RP10000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.0001
          probability:
            span: 1
            value: 0.0001
          return_period: 10000
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS18MS (18 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS18MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS20MS (20 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS20MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS25MS (25 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS25MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS30MS (30 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS30MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS33MS (33 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS33MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS35MS (35 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS35MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS40MS (40 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS40MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS42MS (42 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS42MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS45MS (45 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS45MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS50MS (50 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS50MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS55MS (55 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS55MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS58MS (58 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS58MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS60MS (60 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS60MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS65MS (65 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS65MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS70MS (70 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS70MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    - calculation_method: simulated
      description: 'STORM Fixed Wind Speeds: return period (years) for fixed wind
        speed WS75MS (75 m/s) on ~10 km grids for all ocean basins (available as GeoTIFF
        tiles and gridded NetCDF variants, including multi-model and MEDIAN products).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: STORM_FIXED_WIND_SPEEDS
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: WS75MS
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: null
          return_period: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: STORM_FIXED_RETURN_PERIODS
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    - classification: null
      id: STORM_FIXED_WIND_SPEEDS
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    - classification: null
      id: Cities_Tables
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    - classification: null
      id: Islands_Tables
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_storm_cc_tropical_cyclone
    occurrence_range: 1/10 to 1/10000 years
    seasonality: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Tropical cyclone wind speed return period grids produced using the
    STORM (Synthetic Tropical cyclOne geneRation Model) model. Historical storm tracks
    from IBTrACS were used to calibrate a statistical-physical parametric wind field
    model. Wind speed return period surfaces were computed from 10,000-year synthetic
    track simulations using ERA5 reanalysis data as the atmospheric background. Both
    historical baseline and climate change scenario variants were produced.
  sources:
  - id: source_1
    license: CC-BY-4.0
    name: ERA5 - ECMWF Reanalysis v5
    risk_data_type: null
    type: dataset
    url: https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5
    used_in: hazard
  - id: source_2
    license: https://creativecommons.org/publicdomain/zero/1.0/
    name: International Best Track Archive for Climate Stewardship (IBTrACS)
    risk_data_type: null
    type: dataset
    url: https://www.ncei.noaa.gov/products/international-best-track-archive
    used_in: hazard
  - id: source_3
    license: https://creativecommons.org/publicdomain/zero/1.0/
    name: STORM - Synthetic Tropical cyclOne geneRation Model
    risk_data_type: null
    type: dataset
    url: https://data.4tu.nl/datasets/0ea98bdd-5772-4da8-ae97-99735e891aff
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: STORM - Synthetic Tropical cyclOne geneRation Model
  url: https://data.4tu.nl/datasets/0ea98bdd-5772-4da8-ae97-99735e891aff
publisher:
  affiliation: null
  email: researchdata@4tu.nl
  name: 4TU.ResearchData
  url: https://data.4tu.nl/
purpose: To supply consistent, high-resolution tropical-cyclone wind hazard metrics
  for present climate and climate change scenarios that support risk assessment, engineering
  design, and adaptation planning using a common methodology (Weibull plotting) across
  basins and for selected cities and islands.
referenced_by:
- author_names:
  - Nadia Bloemendaal
  - Ivan D. Haigh
  - Hans de Moel
  - Sanne Muis
  - Reindert J. Haarsma
  - Jeroen C. J. H. Aerts
  date_published: '2020-02-06'
  doi: https://doi.org/10.1038/s41597-020-0381-2
  id: reference_1
  name: Generation of a global synthetic tropical cyclone hazard dataset using STORM
  url: https://www.nature.com/articles/s41597-020-0381-2
- author_names:
  - Nadia Bloemendaal
  - Hans de Moel
  - Sanne Muis
  - Jeroen C. J. H. Aerts
  - Ivan D. Haigh
  date_published: '2020-11-10'
  doi: https://doi.org/10.1038/s41597-020-00720-x
  id: reference_2
  name: Estimation of global tropical cyclone wind speed probabilities using the STORM
    dataset
  url: https://www.nature.com/articles/s41597-020-00720-x
resources:
- access_url: https://data.4tu.nl/datasets/0ea98bdd-5772-4da8-ae97-99735e891aff/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Basin reference layer listing the six TC basins used across the STORM
    products: EP (Eastern Pacific), NA (North Atlantic), NI (North Indian), SI (South
    Indian), SP (South Pacific), WP (Western Pacific)'
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/e4d92161-214a-4df7-a2fb-533825b1d46e
  format: null
  id: resource_1
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Basins of STORM IBTrACS dataset (KML)
- access_url: https://data.4tu.nl/datasets/0ea98bdd-5772-4da8-ae97-99735e891aff/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Workbook with two sheets for events within 100 km of 18 predefined
    coastal cities: (1) wind speed at fixed return periods, and (2) return period
    at fixed wind speeds (5 m/s steps plus Saffir-Simpson thresholds).'
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/d08e9a54-a5bf-442a-ac3c-69ec1f9a0f59
  format: null
  id: resource_2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STORM Cities: TC wind-speed return periods (present)'
- access_url: https://data.4tu.nl/datasets/0ea98bdd-5772-4da8-ae97-99735e891aff/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Per-basin ~10 km grids of maximum wind speed (m/s) at fixed return
    periods (10-10,000 yr), including mean, standard deviation, and 5-95% confidence
    intervals over 1,000 realizations.
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/0b98c6f5-c7af-45bb-bb6e-dac53e1b8d55
  format: null
  id: resource_3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Return Periods (present, gridded)
- access_url: https://data.4tu.nl/datasets/0ea98bdd-5772-4da8-ae97-99735e891aff/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Per-basin ~10 km grids of return period (years) at fixed wind speeds
    (20-75 m/s at 5 m/s steps, plus 18, 33, 42, 58 m/s), including mean, standard
    deviation, and 5-95% confidence intervals over 1,000 realizations.
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/3c839d73-e6c0-4d63-ae03-c0d05e734d57
  format: null
  id: resource_4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Wind Speeds (present, gridded)
- access_url: https://data.4tu.nl/datasets/0ea98bdd-5772-4da8-ae97-99735e891aff/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Workbook with two sheets for events within 100 km of island capitals
    (SIDS and others): (1) wind speed at fixed return periods, and (2) return period
    at fixed wind speeds (5 m/s steps plus Saffir-Simpson thresholds).'
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/f537c00b-4019-42da-bd13-e4bcb49c8aa3
  format: null
  id: resource_5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STORM Islands: TC wind-speed return periods (present)'
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of 18 coastal cities
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/c064030c-e60d-4394-9c46-4b1c81c6fe3f
  format: null
  id: resource_storm_cities_cmcc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STORM Cities: TC wind-speed return periods - CMCC-CM2-VHR4'
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of 18 coastal cities
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/c97acdc5-ce00-445e-89fb-9eb0854561b7
  format: null
  id: resource_storm_cities_cnrm
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STORM Cities: TC wind-speed return periods - CNRM-CM6-1-HR'
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of 18 coastal cities
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/4c5743bf-45bb-4930-bd1a-dc1913ba69a9
  format: null
  id: resource_storm_cities_ecearth
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STORM Cities: TC wind-speed return periods - EC-Earth3P-HR'
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of 18 coastal cities
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/79e8563e-54bf-4d52-a3a0-d5ae04be3a06
  format: null
  id: resource_storm_cities_hadgem
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STORM Cities: TC wind-speed return periods - HadGEM3-GC31-HM'
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: maximum wind speed (m/s) at fixed return periods on
    ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/2a3759e8-f4ad-4190-abb3-434ad5c4679b
  format: null
  id: resource_storm_frp_tif_cmcc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Return Periods (GeoTIFF tiles) - CMCC-CM2-VHR4
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: maximum wind speed (m/s) at fixed return periods on
    ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/c460a0c8-f918-4ede-a734-75e77e99b102
  format: null
  id: resource_storm_frp_tif_cnrm
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Return Periods (GeoTIFF tiles) - CNRM-CM6-1-HR
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: maximum wind speed (m/s) at fixed return periods on
    ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/304d1441-bd71-47c7-8231-b20253c1cc2a
  format: null
  id: resource_storm_frp_tif_ecearth
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Return Periods (GeoTIFF tiles) - EC-Earth3P-HR
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: maximum wind speed (m/s) at fixed return periods on
    ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/856f9530-56d7-489e-8005-18ae36db4804
  format: null
  id: resource_storm_frp_tif_hadgem
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Return Periods (GeoTIFF tiles) - HADGEM3-GC31-HM
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: maximum wind speed (m/s) at fixed return periods on
    ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/9740b235-c2fe-4677-a8b9-f90eb13e4938
  format: null
  id: resource_storm_frp_tif_median
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Return Periods (GeoTIFF tiles) - MEDIAN
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Gridded dataset: maximum wind speed (m/s) at fixed return periods
    on ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/3b7dde9d-bff7-4d96-9024-e8169e8effc0
  format: null
  id: resource_storm_frp_grid_cmcc
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Return Periods (gridded) - CMCC
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Gridded dataset: maximum wind speed (m/s) at fixed return periods
    on ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/cb4bbaaa-8d70-48f5-865d-d3514ba15503
  format: null
  id: resource_storm_frp_grid_cnrm
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Return Periods (gridded) - CNRM
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Gridded dataset: maximum wind speed (m/s) at fixed return periods
    on ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/9e5fb7fe-12b9-4197-ad78-e4e0e2b1c754
  format: null
  id: resource_storm_frp_grid_ecearth
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Return Periods (gridded) - EC-Earth
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Gridded dataset: maximum wind speed (m/s) at fixed return periods
    on ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/5f7fc711-990c-4c95-a071-c17f648d43bb
  format: null
  id: resource_storm_frp_grid_hadgem
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Return Periods (gridded) - HadGEM
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Gridded dataset: maximum wind speed (m/s) at fixed return periods
    on ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/e3b74bbd-04df-4399-ab23-a13af5be4a9b
  format: null
  id: resource_storm_frp_grid_median
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: ~10km resolution grid cells
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Return Periods (gridded) - MEDIAN
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/df247ab2-7565-4888-b5a9-2ccd31d9c90f
  format: null
  id: resource_storm_fws_tif_cmcc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Wind Speeds (GeoTIFF tiles) - CMCC-CM2-VHR4
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/43ce1a8f-914a-414c-b949-884e06616301
  format: null
  id: resource_storm_fws_tif_cnrm
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Wind Speeds (GeoTIFF tiles) - CNRM-CM6-1-HR
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/ac3fd12d-c21d-406e-8e2e-bd212ee9f817
  format: null
  id: resource_storm_fws_tif_ecearth
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Wind Speeds (GeoTIFF tiles) - EC-Earth3P-HR
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/a7e915a4-ee2a-44d7-8e91-8920bff34f16
  format: null
  id: resource_storm_fws_tif_hadgem
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Wind Speeds (GeoTIFF tiles) - HADGEM3-GC31-HM
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/6107d9db-5e6f-4ee7-b113-ce66c1e73aa1
  format: null
  id: resource_storm_fws_tif_median
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Wind Speeds (GeoTIFF tiles) - MEDIAN
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Gridded dataset: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/02773d34-5e47-41be-bf15-5a5c537ae78c
  format: null
  id: resource_storm_fws_grid_cmcc
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Wind Speeds (gridded) - CMCC
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Gridded dataset: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/4b2b73b2-225e-4bcf-af5b-5e048501b354
  format: null
  id: resource_storm_fws_grid_cnrm
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Wind Speeds (gridded) - CNRM
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Gridded dataset: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/3e489cb4-049c-43d3-ab9e-ab40d9e3f375
  format: null
  id: resource_storm_fws_grid_ecearth
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Wind Speeds (gridded) - EC-Earth
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Gridded dataset: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/c1da70b1-64d5-4151-aa9c-2ae15bd89de6
  format: null
  id: resource_storm_fws_grid_hadgem3
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Wind Speeds (gridded) - HadGEM3
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Gridded dataset: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/6107d9db-5e6f-4ee7-b113-ce66c1e73aa1
  format: null
  id: resource_storm_fws_grid_median
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: STORM Fixed Wind Speeds (gridded) - MEDIAN
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of island capitals (SIDS and
    others)
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/4a961e63-bb03-4766-ae91-7cf1deb72ff8
  format: null
  id: resource_storm_islands_cmcc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STORM Islands: TC wind-speed return periods - CMCC-CM2-VHR4'
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of island capitals (SIDS and
    others)
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/0632e12d-270e-4496-9bc8-650cb47be71d
  format: null
  id: resource_storm_islands_cnrm
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STORM Islands: TC wind-speed return periods - CNRM-CM6-1-HR'
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of island capitals (SIDS and
    others)
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/43396cb0-72bd-46f0-97f2-006a2e31068f
  format: null
  id: resource_storm_islands_ecearth
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STORM Islands: TC wind-speed return periods - EC-Earth3P-HR'
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of island capitals (SIDS and
    others)
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/39e5571c-efd1-41ee-a4f2-1d94e792f1ed
  format: null
  id: resource_storm_islands_hadgem
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STORM Islands: TC wind-speed return periods - HadGEM3-GC31-HM'
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-nismod_stormtcwshistcc
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: STORM tropical cyclone wind speed return periods (present and climate change)
version: '4'
vulnerability: null
---

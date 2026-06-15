---
attributions:
- entity:
    affiliation: null
    email: dccinfo@rws.nl
    name: Dutch Ministry of Infrastructure and Water Management
    url: https://www.rijkswaterstaat.nl/en
  id: attribution_funder
  role: funder
- entity:
    affiliation: null
    email: info@vu.nl
    name: Vrije Universiteit Amsterdam Institute for Environmental Studies
    url: https://vu.nl/en/about-vu/research-institutes/ivm
  id: attribution_collaborator_1
  role: collaborator
- entity:
    affiliation: null
    email: info@deltares.nl
    name: Deltares
    url: https://www.deltares.nl/en
  id: attribution_collaborator_2
  role: collaborator
- entity:
    affiliation: null
    email: info@uu.nl
    name: Utrecht University
    url: https://www.uu.nl/en
  id: attribution_collaborator_3
  role: collaborator
- entity:
    affiliation: null
    email: info@pbl.nl
    name: PBL Netherlands Environmental Assessment Agency
    url: https://www.pbl.nl/en
  id: attribution_collaborator_4
  role: collaborator
catalog: null
contact_point:
  affiliation: null
  email: samantha.kuzma@wri.org
  name: Samantha Kuzma
  url: https://www.wri.org/data/aqueduct-floods-hazard-maps
creator:
  affiliation: null
  email: samantha.kuzma@wri.org
  name: World Resources Institute
  url: https://www.wri.org/data/aqueduct-floods-hazard-maps
dataset_id: rdls_hzd-nismod_aqueductfloodshazard
description: Gridded flood inundation hazard maps showing riverine and coastal flood
  risks globally, with inundation depth measurements in meters for multiple return
  periods (2-year to 1000-year floods) under current baseline conditions and future
  climate projections for 2030, 2050, and 2080.
details: The dataset uses hydrological data from 1960-1999 for current flood scenarios
  and incorporates five Global Climate Models (GCMs) from CMIP5 under two climate
  scenarios (RCP4.5 and RCP8.5) and socio-economic pathways (SSP2 and SSP3) from the
  IPCC Fifth Assessment Report for future projections. The dataset is recommended
  for large-scale regional analysis, preliminary assessments, and evaluating relative
  changes in flood impacts under different climate scenarios. It is not suitable for
  detailed property-specific flood inundation mapping, analyzing flat lowland rivers
  with significant backwater effects, or assessing the impact of hydraulic structures.
  Flood hazard maps represent situations with no flood protection measures and may
  overestimate flood extent where protection infrastructure exists.
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 378
      events:
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          historical baseline conditions without subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          historical baseline conditions without subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          historical baseline conditions without subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          historical baseline conditions without subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          historical baseline conditions without subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          historical baseline conditions without subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          historical baseline conditions without subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          historical baseline conditions without subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          historical baseline conditions without subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          historical baseline conditions without subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          historical baseline conditions without subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          historical baseline conditions without subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          historical baseline conditions without subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          historical baseline conditions without subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          historical baseline conditions without subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          historical baseline conditions without subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          historical baseline conditions without subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          historical baseline conditions without subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          historical baseline conditions without subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          historical baseline conditions without subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          historical baseline conditions without subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          historical baseline conditions without subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          historical baseline conditions without subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          historical baseline conditions without subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          historical baseline conditions without subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          historical baseline conditions without subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          historical baseline conditions without subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_nosub_hist_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          historical baseline conditions with subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          historical baseline conditions with subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          historical baseline conditions with subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          historical baseline conditions with subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          historical baseline conditions with subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          historical baseline conditions with subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          historical baseline conditions with subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          historical baseline conditions with subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          historical baseline conditions with subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          historical baseline conditions with subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          historical baseline conditions with subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          historical baseline conditions with subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          historical baseline conditions with subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          historical baseline conditions with subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          historical baseline conditions with subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          historical baseline conditions with subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          historical baseline conditions with subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          historical baseline conditions with subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          historical baseline conditions with subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          historical baseline conditions with subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          historical baseline conditions with subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          historical baseline conditions with subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          historical baseline conditions with subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          historical baseline conditions with subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          historical baseline conditions with subsidence (95th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          historical baseline conditions with subsidence (5th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          historical baseline conditions with subsidence (50th percentile sea level
          rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_historical_wtsub_hist_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2030_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2050_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_nosub_2080_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2030_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2050_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp4p5_wtsub_2080_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2030 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2030_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2050 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2050_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (95th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (5th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2080 without subsidence (50th percentile
          sea level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_nosub_2080_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2030 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2030_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2050 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2050_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0002_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0002_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 2-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0002_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0005_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0005_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 5-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0005_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0010_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0010_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 10-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0010_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0025_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0025_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 25-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0025_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0050_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0050_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 50-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0050_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0100_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0100_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 100-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0100_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0250_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0250_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 250-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0250_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0500_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0500_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 500-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp0500_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (95th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp1000_0
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (5th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp1000_0_perc_05
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Coastal flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario for year 2080 with subsidence (50th percentile sea
          level rise)
        disaster_identifiers: []
        hazard:
          classification: null
          id: coastal_flood_hazard_ref
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: inuncoast_rcp8p5_wtsub_2080_rp1000_0_perc_50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      frequency_distribution: null
      hazards:
      - classification: null
        id: coastal_flood_hazard_ref
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_set_coastal_flood
      occurrence_range: Return periods from 2, 5, 10, 25, 50, 100, 250, 500, and 1000
        years
      seasonality: null
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 279
      events:
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          historical baseline conditions
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_historical_000000000WATCH_hist_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          historical baseline conditions
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_historical_000000000WATCH_hist_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          historical baseline conditions
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_historical_000000000WATCH_hist_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          historical baseline conditions
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_historical_000000000WATCH_hist_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          historical baseline conditions
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_historical_000000000WATCH_hist_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          historical baseline conditions
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_historical_000000000WATCH_hist_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          historical baseline conditions
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_historical_000000000WATCH_hist_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          historical baseline conditions
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_historical_000000000WATCH_hist_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          historical baseline conditions
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_historical_000000000WATCH_hist_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2030_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2030_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2030_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2030_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2030_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2030_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2030_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2030_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2030_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2050_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2050_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2050_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2050_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2050_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2050_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2050_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2050_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2050_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2080_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2080_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2080_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2080_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2080_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2080_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2080_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2080_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00000NorESM1-M_2080_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2030_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2030_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2030_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2030_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2030_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2030_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2030_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2030_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2030_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2050_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2050_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2050_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2050_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2050_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2050_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2050_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2050_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2050_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2080_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2080_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2080_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2080_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2080_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2080_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2080_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2080_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000GFDL-ESM2M_2080_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2030_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2030_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2030_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2030_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2030_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2030_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2030_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2030_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2030_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2050_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2050_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2050_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2050_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2050_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2050_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2050_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2050_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2050_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2080_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2080_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2080_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2080_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2080_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2080_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2080_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2080_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_0000HadGEM2-ES_2080_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2030_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2030_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2030_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2030_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2030_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2030_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2030_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2030_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2030_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2050_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2050_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2050_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2050_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2050_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2050_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2050_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2050_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2050_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2080_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2080_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2080_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2080_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2080_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2080_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2080_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2080_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_00IPSL-CM5A-LR_2080_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2030_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2030_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2030_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2030_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2030_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2030_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2030_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2030_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2030_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2050_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2050_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2050_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2050_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2050_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2050_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2050_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2050_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2050_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2080_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2080_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2080_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2080_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2080_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2080_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2080_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2080_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP4.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp4p5_MIROC-ESM-CHEM_2080_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2030_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2030_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2030_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2030_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2030_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2030_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2030_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2030_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2030_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2050_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2050_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2050_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2050_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2050_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2050_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2050_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2050_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2050_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2080_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2080_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2080_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2080_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2080_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2080_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2080_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2080_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using NorESM1-M model (Bjerknes Centre for Climate
          Research, Norwegian Meteorological Institute) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00000NorESM1-M_2080_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2030_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2030_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2030_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2030_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2030_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2030_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2030_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2030_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2030_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2050_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2050_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2050_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2050_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2050_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2050_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2050_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2050_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2050_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2080_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2080_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2080_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2080_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2080_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2080_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2080_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2080_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using GFDL-ESM2M model (Geophysical Fluid Dynamics
          Laboratory (NOAA)) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000GFDL-ESM2M_2080_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2030_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2030_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2030_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2030_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2030_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2030_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2030_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2030_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2030_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2050_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2050_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2050_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2050_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2050_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2050_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2050_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2050_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2050_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2080_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2080_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2080_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2080_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2080_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2080_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2080_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2080_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using HadGEM2-ES model (Met Office Hadley Centre)
          for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_0000HadGEM2-ES_2080_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2030_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2030_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2030_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2030_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2030_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2030_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2030_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2030_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2030_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2050_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2050_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2050_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2050_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2050_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2050_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2050_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2050_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2050_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2080_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2080_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2080_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2080_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2080_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2080_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2080_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2080_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using IPSL-CM5A-LR model (Institut Pierre Simon
          Laplace) for year 2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_00IPSL-CM5A-LR_2080_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2030_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2030_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2030_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2030_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2030_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2030_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2030_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2030_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2030
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2030_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2050_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2050_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2050_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2050_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2050_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2050_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2050_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2050_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2050
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2050_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      - calculation_method: simulated
        description: Riverine flood inundation depth for 2-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2080_rp0002
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.5
            probability:
              span: 50
              value: 1
            return_period: 2
      - calculation_method: simulated
        description: Riverine flood inundation depth for 5-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2080_rp0005
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability:
              span: 50
              value: 1
            return_period: 5
      - calculation_method: simulated
        description: Riverine flood inundation depth for 10-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2080_rp0010
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability:
              span: 50
              value: 0.995
            return_period: 10
      - calculation_method: simulated
        description: Riverine flood inundation depth for 25-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2080_rp0025
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.04
            probability:
              span: 50
              value: 0.87
            return_period: 25
      - calculation_method: simulated
        description: Riverine flood inundation depth for 50-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2080_rp0050
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability:
              span: 50
              value: 0.636
            return_period: 50
      - calculation_method: simulated
        description: Riverine flood inundation depth for 100-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2080_rp0100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 50
              value: 0.395
            return_period: 100
      - calculation_method: simulated
        description: Riverine flood inundation depth for 250-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2080_rp0250
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.004
            probability:
              span: 50
              value: 0.182
            return_period: 250
      - calculation_method: simulated
        description: Riverine flood inundation depth for 500-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2080_rp0500
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability:
              span: 50
              value: 0.095
            return_period: 500
      - calculation_method: simulated
        description: Riverine flood inundation depth for 1000-year return period under
          RCP8.5 climate scenario using MIROC-ESM-CHEM model (Atmosphere and Ocean
          Research Institute (The University of Tokyo), National Institute for Environmental
          Studies, and Japan Agency for Marine-Earth Science and Technology) for year
          2080
        disaster_identifiers: []
        hazard:
          classification: null
          id: river_flood_hazard_ref
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: inunriver_rcp8p5_MIROC-ESM-CHEM_2080_rp1000
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 50
              value: 0.049
            return_period: 1000
      frequency_distribution: null
      hazards:
      - classification: null
        id: river_flood_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_river_flood
      occurrence_range: Return periods from 2, 5, 10, 25, 50, 100, 250, 500, and 1000
        years
      seasonality: null
  event_sets_count: 2
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Global river flood hazard inundation layers produced by the Aqueduct
    Floods model (Ward et al., World Resources Institute). A global hydrodynamic model
    driven by multi-decadal river discharge simulations was calibrated against observed
    gauge records and validated against historical flood events. Return period inundation
    extents and water depths were computed using extreme value statistics applied
    to simulated discharge time series.
  sources:
  - id: source_1
    license: https://creativecommons.org/licenses/by/4.0/
    name: Aqueduct Floods Methodology
    risk_data_type: null
    type: model
    url: https://www.wri.org/research/aqueduct-floods-methodology
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: Aqueduct
  url: https://www.wri.org/aqueduct
publisher:
  affiliation: null
  email: samantha.kuzma@wri.org
  name: World Resources Institute
  url: https://www.wri.org/data/aqueduct-floods-hazard-maps
purpose: The dataset was created to measure and map water-related flood risks worldwide
  to help decision-makers protect communities, target investments, and mitigate future
  flood risks. It enables users to conduct comprehensive cost-benefit analysis to
  evaluate the value of flood protection strategies, including dike protection measures.
referenced_by:
- author_names:
  - Philip J. Ward
  - Hessel C. Winsemius
  - Samantha Kuzma
  - Marc F.P. Bierkens
  - Arno Bouwman
  - Hans De Moel
  - "Andr\xE9s D\xEDaz Loaiza"
  - Dirk Eilander
  - Johanna Englhardt
  - Gilles Erkens
  - Eskedar Tafete Gebremedhin
  - Charles Iceland
  - Henk Kooi
  - Willem Ligtvoet
  - Sanne Muis
  - Paolo Scussolini
  - Edwin H. Sutanudjaja
  - Rens Van Beek
  - Bas Van Bemmel
  - Jolien Van Huijstee
  - Frank Van Rijn
  - Bregje Van Wesenbeeck
  - Deepak Vatvani
  - Martin Verlaan
  - Timothy Tiggeloven
  - Tianyi Luo
  date_published: '2020-01-01'
  doi: null
  id: reference_1
  name: 'AQUEDUCT FLOODS METHODOLOGY: TECHNICAL NOTE'
  url: https://www.wri.org/research/aqueduct-floods-methodology
resources:
- access_url: https://wri-projects.s3.amazonaws.com/AqueductFloodTool/download/v2/index.html
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global flood inundation depth maps for coastal and riverine hazards
    derived from the WRI Aqueduct Flood Tool. This collection encompasses historical
    baseline conditions and future climate projections (RCP4.5 and RCP8.5) for the
    years 2030, 2050, and 2080. It includes scenarios with and without land subsidence
    across multiple return periods (2, 5, 10, 25, 50, 100, 250, 500, and 1000 years).
    The riverine models utilize various GCMs including NorESM1-M, GFDL-ESM2M, HadGEM2-ES,
    IPSL-CM5A-LR, and MIROC-ESM-CHEM.
  download_url: https://wri-projects.s3.amazonaws.com/AqueductFloodTool/download/v2/index.html
  format: null
  id: wri_aqueduct_flood_inundation_depth_collection
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal:
    central_year: null
    duration: P70Y
    end: '2080'
    start: '2010'
  temporal_resolution: null
  title: WRI Aqueduct Coastal and Riverine Flood Inundation Depth (Historical and
    Future Projections)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-nismod_aqueductfloodshazard
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
title: Aqueduct Floods Hazard
version: '2'
vulnerability: null
---

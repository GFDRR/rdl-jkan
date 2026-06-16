---
attributions:
- entity:
    affiliation: null
    email: franghieri@worldbank.org
    name: Federica Ranghieri
    url: null
  id: '0'
  role: world_bank_team_lead
- entity:
    affiliation: null
    email: dfallesen@worldbank.org
    name: Ditte Fallesen
    url: null
  id: '1'
  role: world_bank_team_lead
- entity:
    affiliation: null
    email: bjongman@worldbank.org
    name: Brandan Jongman
    url: null
  id: '2'
  role: world_bank_team_lead
catalog: null
contact_point:
  affiliation: null
  email: pchrzanowski@worldbank.org
  name: Pierre Chrzanowski
  url: null
creator:
  affiliation: null
  email: null
  name: GFDRR
  url: https://www.gfdrr.org
dataset_id: rdls_hzd-afg_gfdrr_earthquakehazard
description: Earthquake hazard map representing Peak ground acceleration (PGA-g) for
  seven return period scenarios.
details: "To better understand natural hazard and disaster risk, the World Bank and\
  \ Global Facility for Disaster Reduction and Recovery (GFDRR) supported the development\
  \ of new \uFB02uvial \uFB02ood, \uFB02ash \uFB02ood, drought, landslide, avalanche\
  \ and seismic risk information in Afghanistan, as well as a frst-order analysis\
  \ of the costs and benefts of resilient reconstruction and risk reduction strategies.\
  \ This publication describes the applied methods and main results of the project."
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 7
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: '0'
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: '0'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: '0'
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: '1'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: '0'
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: '2'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: '0'
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: '3'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 250
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: '0'
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: '4'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 500
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: '0'
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: '5'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 1000
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: '0'
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: '6'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 2500
    frequency_distribution: null
    hazards:
    - classification: null
      id: '0'
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: '0'
    occurrence_range: 10, 50, 100, 250, 500, 1000, 2.500 years
    seasonality: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Afghanistan Multi-hazard risk assessment
  url: null
publisher:
  affiliation: null
  email: null
  name: GFDRR
  url: https://www.gfdrr.org
purpose: These maps have been derived on a nation-wide scale for the purpose of identifying
  high risk- areas on the district and provincial scale, from which decisions can
  be made on allocating efforts for more detailed site specific hazard and risk analysis.
  Use of this information on smaller scales should be applied with care. Importantly
  for on a local scale, it is often the case that more detailed case history and hazard
  information is required to perform such hazard and risk modelling, particularly
  where applied to dimension mitigation structures or strategies.
referenced_by:
- author_names:
  - Federica Ranghieri
  - Ditte Fallesen
  - Brenden Jongman
  - Guillermo Siercke
  - Abdul Azim Doosti
  - Julian Palma
  - Simone Balog
  - Sayed Sharifullah Mashahid
  - Erika Vargas
  date_published: '2018-12-18'
  doi: null
  id: '0'
  name: Afghanistan - Multi-hazard risk assessment
  url: https://www.gfdrr.org/sites/default/files/publication/Afghanistan_MHRA.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32642
  description: Peak ground acceleration (PGA-g) simulated for seven return period
    scenarios (10, 50, 100, 250, 500 , 1000 and 2500 years).
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0050631/DR0065467/hzd-afg-eq.zip
  format: geotiff
  id: '0'
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Earthquake ground shaking hazard scenarios
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-afg_gfdrr_earthquakehazard
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Afghanistan Earthquake hazard
version: '2018'
vulnerability: null
---

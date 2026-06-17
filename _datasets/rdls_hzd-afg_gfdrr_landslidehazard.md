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
dataset_id: rdls_hzd-afg_gfdrr_landslidehazard
description: Earthquake-induced landslide hazard measured as probability of occurrance
  for seven return period scenarios. National hazard assessment and focus on two areas
  (Kabul and Salang pass).
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
    calculation_method: inferred
    event_count: 68
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: '0'
        intensity_measure: Debris flow intensity index
        process: landslide_general
        trigger: null
        type: landslide
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
        intensity_measure: Debris flow intensity index
        process: landslide_general
        trigger: null
        type: landslide
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
        intensity_measure: Debris flow intensity index
        process: landslide_general
        trigger: null
        type: landslide
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
        intensity_measure: Debris flow intensity index
        process: landslide_general
        trigger: null
        type: landslide
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
        intensity_measure: Debris flow intensity index
        process: landslide_general
        trigger: null
        type: landslide
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
        intensity_measure: Debris flow intensity index
        process: landslide_general
        trigger: null
        type: landslide
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
        intensity_measure: Debris flow intensity index
        process: landslide_general
        trigger: null
        type: landslide
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
      intensity_measure: Debris flow intensity index
      process: landslide_general
      trigger: null
      type: landslide
    id: '0'
    occurrence_range: 10, 50, 100, 250, 500, 1000, 2500 years
    seasonality: null
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: '1'
      intensity_measure: Susceptibility index
      process: landslide_general
      trigger: null
      type: landslide
    id: '1'
    occurrence_range: null
    seasonality: null
  type: landslide
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
  description: Simulated Ground Motion process triggered by earthquake measured as
    debris-flow intensity index
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0050634/DR0065476/hzd-afg-ls-eq-rp.zip
  format: geotiff
  id: '0'
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 30
  temporal: null
  temporal_resolution: null
  title: Landslide hazard RP scenarios
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32642
  description: 'Susceptibility map for bedrock landslides in slow evolution (S1),
    bedrock landslides in rapid evolution (S2) and cover material landslides in rapid
    evolution (S3) nationwide, including: rotational slides, translational slides,
    earth flows and lateral spreading.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0050634/DR0065476/hzd-afg-ls-eq-susceptibility.zip
  format: geotiff
  id: '1'
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 30
  temporal: null
  temporal_resolution: null
  title: Landslide susceptibility
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-afg_gfdrr_landslidehazard
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries:
  - description: Kabul District
    id: AFG-KAB
    scheme: ISO 3166-2
    uri: null
  - description: Salang pass
    id: "K\u014Dtal-e S\u0101lang"
    scheme: GEONAMES
    uri: https://www.geonames.org/1127859/kotal-e-salang.html
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Afghanistan Landslide hazard
version: '2018'
vulnerability: null
---

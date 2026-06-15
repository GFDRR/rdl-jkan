---
attributions:
- entity:
    affiliation: null
    email: lloeschner@worldbank.org
    name: Lukas Loeschner
    url: null
  id: '0'
  role: world_bank_team_lead
- entity:
    affiliation: null
    email: mamadio@worldbank.org
    name: Mattia Amadio
    url: null
  id: '1'
  role: author
catalog: World Bank Data Catalog
contact_point:
  affiliation: null
  email: lloeschner@worldbank.org
  name: Lukas Loeschner
  url: null
creator:
  affiliation: null
  email: mamadio@worldbank.org
  name: Mattia Amadio
  url: null
dataset_id: rdls_hzd-ssd_gfdrr_earthquakehazard
description: Earthquake hazard intensity (g) for Sub Saharan Africa from Global Earthquake
  Model (GEM) 2016
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    earthquake:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 4
      events:
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: EQ
          intensity_measure: PGA:g
          process: ground_motion
          trigger: null
          type: earthquake
        id: '100'
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
          id: EQ
          intensity_measure: PGA:g
          process: ground_motion
          trigger: null
          type: earthquake
        id: '475'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 475
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: EQ
          intensity_measure: PGA:g
          process: ground_motion
          trigger: null
          type: earthquake
        id: '975'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 975
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: EQ
          intensity_measure: PGA:g
          process: ground_motion
          trigger: null
          type: earthquake
        id: '2475'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 2475
      frequency_distribution: null
      hazards:
      - classification: null
        id: EQ
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: GEM
      occurrence_range: 100, 475, 975, 2475 years
      seasonality: null
  event_sets_count: 1
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: South Sudan Multi-hazard risk assessment
  url: null
publisher:
  affiliation: null
  email: null
  name: GFDRR
  url: https://www.gfdrr.org
purpose: The results of the analysis contribute to the production of knowledge for
  disaster risk management (DRM) to support the World Bank's operational teams in
  their in-country engagements. Specifcally, the key fndings of this study allow to
  rank South Sudan states in terms of natural disasters risk, and to identify the
  most critical components for each area. The output of this assessment includes a
  geodatabase which contains both the key primary data and all the resulting maps
  produced by the analysis, allowing risk analysts and managers to explore them in
  detail using GIS software.
referenced_by:
- author_names:
  - Rina Meutia
  - Lukas Loeschner
  - Makiko Watanabe
  - Meskerem Brhane
  - Mattia Amadio
  date_published: '2020-09-24'
  doi: null
  id: '0'
  name: 'Disasters, Conflict, and Displacement : Intersectional Risks in South Sudan
    (Vol. 2)'
  url: http://documents1.worldbank.org/curated/en/570701601009027965/pdf/Summary.pdf
resources:
- access_url: https://datacatalog.worldbank.org/search/dataset/0042411/South-Sudan-Earthquake--ground-shaking--hazard
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Earthquake hazard intensity (g) for Sub Saharan Africa from Global
    Earthquake Model (GEM) 2016 for RP 100, 475, 975, 2475 years.
  download_url: null
  format: geotiff
  id: '0'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Earthquake hazard scenarios
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ssd_gfdrr_earthquakehazard
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: South Sudan Earthquake hazard
version: '2019'
vulnerability: null
---

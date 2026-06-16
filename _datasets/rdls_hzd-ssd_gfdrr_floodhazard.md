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
catalog: null
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
dataset_id: rdls_hzd-ssd_gfdrr_floodhazard
description: River flood hazard extent (perimeter) in South Sudan derived from FATHOM
  2019 for RP 5, 20, 100, 250 years.
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 4
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: FL
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: '5'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: FL
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: '20'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 20
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: FL
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
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
        id: FL
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: '250'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 250
    frequency_distribution: null
    hazards:
    - classification: null
      id: FL
      intensity_measure: fl_wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: Fathom2_extents
    occurrence_range: 5, 20, 100, 250 years
    seasonality: null
  - analysis_type: empirical
    calculation_method: observed
    event_count: 1
    events:
    - calculation_method: observed
      description: null
      disaster_identifiers:
      - description: null
        id: FL-2019-000062-SSD
        scheme: GLIDE
        title: null
        uri: null
      hazard:
        classification: null
        id: FL
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: '0'
      occurrence:
        deterministic: null
        empirical:
          return_period: 100
          temporal: null
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: FL
      intensity_measure: fl_wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: Flood_2019
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
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
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: River flood hazard extents for RP 5, 20, 100, 250 years. Derived from
    FATHOM 2019 model.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0042413/DR0053205/hzd-ssd-fl.zip
  format: gpkg
  id: '0'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Flood hazard scenarios (baseline)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Water extent from satellite imagery and flooded locations from events
    occurring Oct-Nov 2019 in South Sudan.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0042413/DR0053206/hzd-ssd-fl-2019.zip
  format: gpkg
  id: '1'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Observed flood water extent (10-11/2019)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ssd_gfdrr_floodhazard
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
title: South Sudan Flood hazard
version: '2019'
vulnerability: null
---

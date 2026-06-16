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
dataset_id: rdls_hzd-ssd_gfdrr_droughthazard
description: Drought hazard for South Sudan measured as Agricultural Stress Index
  (ASI) over a period of 30 years.
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: deterministic
      calculation_method: inferred
      event_count: 1
      events:
      - calculation_method: inferred
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: DR
          intensity_measure: ASI:per
          process: agricultural_drought
          trigger: null
          type: drought
        id: '0'
        occurrence:
          deterministic:
            description: null
            index_criteria: Frequency of droughts affecting 1/3 or 1/2 of cropland
              health.
            thresholds: null
          empirical: null
          probabilistic: null
      frequency_distribution: null
      hazards:
      - classification: null
        id: DR
        intensity_measure: ASI:per
        process: agricultural_drought
        trigger: null
        type: drought
      id: '0'
      occurrence_range: null
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
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Agricultural drought hazard derived from FAO-GIEWS ASI (30 years).
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0042412/DR0053203/hzd-ssd-dr-asi.zip
  format: gpkg
  id: '0'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal:
    central_year: null
    duration: null
    end: '2019'
    start: '1991'
  temporal_resolution: null
  title: Agricultural Stress Index (ASI)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ssd_gfdrr_droughthazard
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
title: South Sudan Drought hazard
version: '2019'
vulnerability: null
---

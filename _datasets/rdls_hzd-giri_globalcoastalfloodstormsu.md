---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNEP-GRID
    url: https://unepgrid.ch/en
  id: '1'
  role: publisher
- entity:
    affiliation: null
    email: null
    name: CIMA
    url: https://www.cimafoundation.org
  id: '2'
  role: creator
- entity:
    affiliation: null
    email: mamadio@worldbank.org
    name: Mattia Amadio
    url: null
  id: '3'
  role: contact_point
- entity:
    affiliation: null
    email: null
    name: CDRI
    url: https://cdri.world/
  id: '4'
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: null
  name: UNEP-GRID
  url: https://unepgrid.ch/en
creator:
  affiliation: null
  email: null
  name: UNEP-GRID
  url: https://unepgrid.ch/en
dataset_id: rdls_hzd-giri_globalcoastalfloodstormsu
description: Datasets containing probabilistic analysis of coastal flood water depth
  (m) at coastline due to storm surge, covering historical and climate change projections
  at the global scale.
details: Storm surge hazard is modeled only along the coastline. The process involves
  generating a grid along the coastline and 5km inland. In fact, no backwater effects
  were modeled, this is only due to the continent's contour map (shapefile) version
  used to create the grid mentioned on the coastline. In this project, Mediterranean
  tropical-like cyclones were not included in the hazard assessment process. We considered
  only tropical cyclones as storms that develop in areas of low pressure over tropical
  oceans, and that are associated with several hazards such as strong winds and storm
  surge. These two hazards were assessed at a global level but given that although
  tropical cyclones are formed along the North Atlantic Ocean but do not occur in
  Europe, neither strong wings nor storm surge were modeled for European countries.
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 7
      events:
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: CF
          intensity_measure: Wd:M
          process: coastal_flood
          trigger:
            process: null
            type: flood
          type: flood
        id: '10'
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
          id: CF
          intensity_measure: Wd:M
          process: coastal_flood
          trigger:
            process: null
            type: flood
          type: flood
        id: '25'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 25
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: CF
          intensity_measure: Wd:M
          process: coastal_flood
          trigger:
            process: null
            type: flood
          type: flood
        id: '50'
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
          id: CF
          intensity_measure: Wd:M
          process: coastal_flood
          trigger:
            process: null
            type: flood
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
          id: CF
          intensity_measure: Wd:M
          process: coastal_flood
          trigger:
            process: null
            type: flood
          type: flood
        id: '250'
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
          id: CF
          intensity_measure: Wd:M
          process: coastal_flood
          trigger:
            process: null
            type: flood
          type: flood
        id: '500'
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
          id: CF
          intensity_measure: Wd:M
          process: coastal_flood
          trigger:
            process: null
            type: flood
          type: flood
        id: '1000'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 1000
      frequency_distribution: null
      hazards:
      - classification: null
        id: CF
        intensity_measure: Wd:M
        process: coastal_flood
        trigger:
          process: coastal_flood
          type: flood
        type: flood
      id: HST
      occurrence_range: Return period 10 to 1,000 years
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
  name: Global Infrastructure Risk Model and Resilience Index (GIRI)
  url: https://giri.unepgrid.ch/
publisher:
  affiliation: null
  email: null
  name: UNEP-GRID
  url: https://unepgrid.ch/en
purpose: null
referenced_by:
- author_names:
  - O.D. Cardona
  - G. A. Bernal
  - C. P. Villegas
  - J. F. Molina
  - S. A. Herrera
  - M. C. Marulanda
  - "D. F. Rinc\u221A\u2265n"
  - S. Grajales
  - P. M. Marulanda
  - D. Gonzalez
  - A. Maskrey
  date_published: '2023-11-01'
  doi: null
  id: reference_SlPfduen
  name: Multi-hazard Disaster Risk Model of Infrastructure and Buildings at the Global
    Level
  url: https://giri.unepgrid.ch/sites/default/files/2023-11/2.4-INGENIAR-CDRI-Background-Report-Risk-model.pdf
resources:
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Collection of historical coastal flood and storm surge hazard maps
  download_url: https://hazards-data.unepgrid.ch/World_Storm_Surge.gpkg
  format: GeoPackage
  id: HST
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Coastal flood hazard (historical)
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Collection of projected coastal flood and storm surge hazard maps under
    climate change scenarios
  download_url: https://hazards-data.unepgrid.ch/World_Storm_Surge_CC.gpkg
  format: GeoPackage
  id: CC
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Coastal flood hazard (climate change)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-giri_globalcoastalfloodstormsu
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
title: Global coastal flood and storm surge hazard
version: '1'
vulnerability: null
---

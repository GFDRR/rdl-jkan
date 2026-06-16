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
    name: Ingeniar
    url: https://ingeniar-risk.com
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
dataset_id: rdls_hzd-giri_globaltropicalcyclonewind
description: Datasets containing probabilistic analysis of tropical cyclone wind speed
  (km/h) covering historical and climate change projections at the global scale.
details: The tropical cyclone wind hazard model uses historical track data and climate
  projections to generate probabilistic wind speed footprints at global scale. Climate
  change scenarios incorporate projected changes in cyclone frequency and intensity
  based on climate models.
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
        id: TC
        intensity_measure: sws_3s:km/h
        process: tropical_cyclone
        trigger: null
        type: strong_wind
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
        id: TC
        intensity_measure: sws_3s:km/h
        process: tropical_cyclone
        trigger: null
        type: strong_wind
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
        id: TC
        intensity_measure: sws_3s:km/h
        process: tropical_cyclone
        trigger: null
        type: strong_wind
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
        id: TC
        intensity_measure: sws_3s:km/h
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '1000'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 1000
    frequency_distribution: user_defined
    hazards:
    - classification: null
      id: TC
      intensity_measure: sws_3s:km/h
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: TC
    occurrence_range: Return period 50 to 1,000 years
    seasonality: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
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
  description: Collection of historical tropical cyclone wind hazard maps
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: HST
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 11100
  temporal: null
  temporal_resolution: null
  title: Tropical cyclone wind hazard (historical)
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Collection of projected tropical cyclone wind hazard maps under climate
    change scenarios
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: CC
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 11100
  temporal: null
  temporal_resolution: null
  title: Tropical cyclone wind hazard (climate change)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-giri_globaltropicalcyclonewind
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
title: Global tropical cyclone wind hazard
version: '1'
vulnerability: null
---

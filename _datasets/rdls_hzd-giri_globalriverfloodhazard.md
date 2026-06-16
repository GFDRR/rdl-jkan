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
dataset_id: rdls_hzd-giri_globalriverfloodhazard
description: Datasets containing probabilistic analysis of river flood maximum water
  depth (m) covering historical and future projections at the global scale.
details: The hydrological model used is the Continuum model (Silvestro et al. 2013
  and 2015). It is a continuous, distributed and physically based hydrological model
  able to reproduce the spatial-temporal evolution of soil moisture, energy fluxes,
  surface soil temperature, evapotranspiration and discharge. Climate dataset used
  for the simulation of basin response are the W5E5 Global Meteorological dataset
  for present climate, and the ISIMIP3b Global Meteorological reanalysis dataset for
  the futur climate. In order to generate flood hazard maps, resulting discharge estimates
  are input to an hydraulic model based on the Manning equation that compute channel
  uniform flow depth. This simplified approach fits to determine flood maps on large
  areas.
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 9
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: FLD
        intensity_measure: Wd:M
        process: fluvial_flood
        trigger: null
        type: flood
      id: RP2
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 2
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: FLD
        intensity_measure: Wd:M
        process: fluvial_flood
        trigger: null
        type: flood
      id: RP5
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
        id: FLD
        intensity_measure: Wd:M
        process: fluvial_flood
        trigger: null
        type: flood
      id: RP10
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
        id: FLD
        intensity_measure: Wd:M
        process: fluvial_flood
        trigger: null
        type: flood
      id: RP25
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
        id: FLD
        intensity_measure: Wd:M
        process: fluvial_flood
        trigger: null
        type: flood
      id: RP50
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
        id: FLD
        intensity_measure: Wd:M
        process: fluvial_flood
        trigger: null
        type: flood
      id: RP100
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
        id: FLD
        intensity_measure: Wd:M
        process: fluvial_flood
        trigger: null
        type: flood
      id: RP200
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 200
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: FLD
        intensity_measure: Wd:M
        process: fluvial_flood
        trigger: null
        type: flood
      id: RP500
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
        id: FLD
        intensity_measure: Wd:M
        process: fluvial_flood
        trigger: null
        type: flood
      id: RP1000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 1000
    frequency_distribution: generalized_extreme_value
    hazards:
    - classification: null
      id: FLD
      intensity_measure: Wd:M
      process: fluvial_flood
      trigger: null
      type: flood
    id: FLOOD_RP
    occurrence_range: Return period 2 to 1,000 years
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
  - L. Alfieri
  - L. Campo
  - S. Gabellani
  - T. Ghizzoni
  - C. Herold
  - A. Libertino
  - E. Trasforini
  - R. Rudari
  date_published: '2023-01-01'
  doi: null
  id: '1'
  name: The GIRI global flood hazard model
  url: https://giri.unepgrid.ch/sites/default/files/2023-09/CIMA_GIRI_Flood_BGpaper.pdf
- author_names: null
  date_published: '2023-01-01'
  doi: null
  id: '2'
  name: Supplement material to the GIRI global flood hazard model
  url: https://giri.unepgrid.ch/sites/default/files/2023-09/CIMA_GIRI_Flood_BGpaper_Supplement.pdf
resources:
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Collection of historical hazard maps
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: HST
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal:
    central_year: null
    duration: null
    end: '2016'
    start: '1979'
  temporal_resolution: null
  title: Flood hazard (historical 1979-2016)
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Collection of projected hazard maps (SSP1)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: PRJ_LB
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal:
    central_year: null
    duration: null
    end: '2100'
    start: '2017'
  temporal_resolution: null
  title: Flood hazard (projected SSP1)
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Collection of projected hazard maps (SSP5)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: PRJ_UB
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal:
    central_year: null
    duration: null
    end: '2100'
    start: '2017'
  temporal_resolution: null
  title: Flood hazard (projected SSP5)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-giri_globalriverfloodhazard
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
title: Global river flood hazard
version: '1'
vulnerability: null
---

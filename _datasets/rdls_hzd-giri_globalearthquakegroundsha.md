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
dataset_id: rdls_hzd-giri_globalearthquakegroundsha
description: Datasets containing probabilistic analysis of earthquake peak ground
  acceleration (PGA) in units of g (gravity). The map has global coverage and a resolution
  of 30' (~55.5 kilometers at the equator).
details: The earthquake hazard model uses probabilistic seismic hazard analysis (PSHA)
  to estimate ground shaking intensity expressed as peak ground acceleration. The
  model incorporates global seismic source zones, historical earthquake catalogs,
  and ground motion prediction equations.
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 5
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
      id: '1000'
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
    id: EQ
    occurrence_range: Return period 100 to 2,475 years
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
  description: Collection of earthquake peak ground acceleration maps for multiple
    return periods
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: EQ
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 55500
  temporal: null
  temporal_resolution: null
  title: Earthquake ground shaking hazard
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-giri_globalearthquakegroundsha
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
title: Global earthquake ground shaking hazard
version: '1'
vulnerability: null
---

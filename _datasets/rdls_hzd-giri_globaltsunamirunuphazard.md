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
dataset_id: rdls_hzd-giri_globaltsunamirunuphazard
description: Dataset containing probabilistic analysis of tsunami run-up height (m)
  at coastline for return period of 475 years at the global scale.
details: The tsunami hazard model estimates run-up heights at the coastline based
  on probabilistic seismic sources and tsunami propagation modeling. The model considers
  submarine earthquakes as the primary tsunami generation mechanism.
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 1
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: TS
        intensity_measure: Rh_tsi:m
        process: tsunami
        trigger: null
        type: tsunami
      id: '475'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 475
    frequency_distribution: null
    hazards:
    - classification: null
      id: TS
      intensity_measure: Rh_tsi:m
      process: tsunami
      trigger: null
      type: tsunami
    id: RP475
    occurrence_range: Return period 475 years
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
  description: Tsunami run-up height at coastline for 475-year return period
  download_url: https://hazards-data.unepgrid.ch/Tsunami_hazard_results.gpkg
  format: GeoPackage
  id: RP475
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tsunami run-up hazard (475-year return period)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-giri_globaltsunamirunuphazard
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
title: Global tsunami run-up hazard
version: '1'
vulnerability: null
---

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
dataset_id: rdls_hzd-giri_globalsusceptibilityclass
description: The landslides susceptibility map indicates the areas of the world that
  are more prone to landslides, both seismic and precipitation-induced.
details: The precipitation-induced landslides susceptibility map for the current climate
  classifies the terrain into five susceptibility classes by combining slope, vegetation,
  lithology, and antecedent rainfall information from global datasets. The susceptibility
  map has global coverage and a resolution of ~90 meters at the equator.
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: inferred
    event_count: 1
    events:
    - calculation_method: inferred
      description: Susceptibility classes of earthquake-triggered landslides from
        1 (very low) to 5 (very high).
      disaster_identifiers: []
      hazard:
        classification: null
        id: LS_EQ
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: '1'
      occurrence:
        deterministic:
          description: null
          index_criteria: Max
          thresholds:
          - 1 (very low)
          - 2 (low)
          - 3 (medium)
          - 4 (high)
          - 5 (very high)
        empirical: null
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: LS_EQ
      intensity_measure: LSI:-
      process: landslide_general
      trigger:
        process: null
        type: earthquake
      type: landslide
    id: LS_EQ
    occurrence_range: null
    seasonality: uniform
  - analysis_type: deterministic
    calculation_method: inferred
    event_count: 1
    events:
    - calculation_method: inferred
      description: Susceptibility classes of earthquake-triggered landslides from
        1 (very low) to 5 (very high).
      disaster_identifiers: []
      hazard:
        classification: null
        id: LS_RF
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: '1'
      occurrence:
        deterministic:
          description: null
          index_criteria: Max
          thresholds:
          - 1 (very low)
          - 2 (low)
          - 3 (medium)
          - 4 (high)
          - 5 (very high)
        empirical: null
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: LS_RF
      intensity_measure: LSI:-
      process: landslide_general
      trigger:
        process: null
        type: convective_storm
      type: landslide
    id: LS_RF
    occurrence_range: null
    seasonality: uniform
  type: landslide
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
  - Rosa M. Palau
  - Farrokh Nadim
  - Eivind Paulsen
  - "Erlend Storr\u221A\u220Fsten"
  date_published: '2003-01-01'
  doi: null
  id: '1'
  name: A new model for global landslide susceptibility assessment and scenario-based
    hazard assessment
  url: https://giri.unepgrid.ch/sites/default/files/2023-06/20230615-NGI_manuscript_GIRI_landlside_hazard_model.pdf
resources:
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: The earthquake-induced landslides susceptibility map indicates the
    areas of the world that are more prone to landslides triggered by earthquakes.
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: EQ_trigger
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Landslide from earthquake trigger
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: The precipitation-induced landslides susceptibility map for the existing
    climate indicates the areas of the world that are more prone to landslides according
    to current precipitation trends
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: RF_trigger-hst
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Landslide from precipitation trigger - Historical
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: The precipitation-induced landslides susceptibility map for the existing
    climate indicates the areas of the world that are more prone to landslides according
    to future precipitation trends (lower bound)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: RF_trigger-ssp1
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Landslide from precipitation trigger - SSP1
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: The precipitation-induced landslides susceptibility map for the existing
    climate indicates the areas of the world that are more prone to landslides according
    to future precipitation trends (upper bound)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: RF_trigger-ssp5
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Landslide from precipitation trigger - SSP5
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-giri_globalsusceptibilityclass
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
title: Global susceptibility class of landslides
version: '1'
vulnerability: null
---

---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission Joint Research Centre
    url: https://data.humdata.org/dataset/nepal-earthquake-severity-index
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Nepal
    url: https://data.humdata.org/dataset/nepal-earthquake-severity-index
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Nepal (inactive)
  url: https://data.humdata.org/dataset/nepal-earthquake-severity-index
creator:
  affiliation: null
  email: null
  name: OCHA Nepal (inactive)
  url: https://data.humdata.org/dataset/nepal-earthquake-severity-index
dataset_id: rdls_hel-npl_ochanpl_earthquakeseverityindex_20150430
description: 'The Nepal Earthquake Severity Index is designed to provide an overview
  of estimated severity of impacts resulting from the earthquake of 25 April 2015.
  It is not a replacement for first hand damage and needs assessment information,
  but can support prioritisation during early stages of the response. It estimates
  severity based on: 1) the intensity of the earthquake; 2) population; 3) vulnerability
  of housing and population. This index will be updated to take account of: validation
  against first hand reports and improvements to the severity model; improved sources
  of data (quality, timeliness and scale); changing requirements as the response continues.
  Version 2 is the latest version of the Index. Please see the Nepal Earthquake Severity
  Index (Version 4 - 30 April 2015) for more information. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/nepal-earthquake-severity-index]'
details: null
exposure:
- asset_type:
    description: Housing stock classified by structural vulnerability
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population exposed to earthquake ground shaking
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The Nepal Earthquake Severity Index integrates observed ground motion
    intensity from the 25 April 2015 earthquake with gridded population data and housing
    vulnerability assessments to produce a composite severity index. The methodology
    follows the INFORM framework, combining hazard intensity, exposure, and vulnerability
    to estimate spatial patterns of earthquake impact severity for early-stage response
    prioritization.
  sources:
  - id: source_1
    license: null
    name: European Commission Joint Research Centre
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OCHA Nepal
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nepal-earthquake-severity-index
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Estimated severity of building damage from earthquake ground shaking
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: damage
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Estimated population affected by earthquake severity
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: null
      trigger: null
      type: earthquake
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: http://www.inform-index.org/InDepth
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: http://www.inform-index.org/In-depth/Methodology
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal Earthquake Severity Index (Excel file (32MB))
  download_url: https://docs.google.com/uc?id=0BxQd-YLTwrcnVkw1dWJZM0UxVTQ&export=download
  format: null
  id: resource_16614d38
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nepal Earthquake Severity Index Latest Version
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-npl_ochanpl_earthquakeseverityindex_20150430
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-04-30'
temporal_resolution: null
title: Nepal Earthquake Severity Index
version: null
vulnerability: null
---

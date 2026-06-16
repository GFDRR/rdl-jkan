---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus-EMS
    url: https://data.humdata.org/dataset/wildfires-south-of-beirut-in-aley-and-chouf-districts-lebanon
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/wildfires-south-of-beirut-in-aley-and-chouf-districts-lebanon
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-south-of-beirut-in-aley-and-chouf-districts-lebanon
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-south-of-beirut-in-aley-and-chouf-districts-lebanon
dataset_id: rdls_hl-lbn_unosat_wildfiressouthbeirutaleyc_20191021
description: 'UNOSAT code: FR20191016LBN This map illustrates satellite-detected burned
  areas in Aley and Chouf districts, in Lebanon, based on SPOT-6 imagery acquired
  on 19 October 2019. Approximately 1275 ha of potentially burned areas were detected
  by Copernicus-EMS as of 17 October 2019 (orange) and additional 92 ha of burned
  were detected by UNOSAT as of 19 October 2019 (red), which is equivalent to approximately
  7% increase in affected surface area. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wildfires-south-of-beirut-in-aley-and-chouf-districts-lebanon]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Satellite imagery from SPOT-6 acquired on 19 October 2019 was analyzed
    by UNOSAT analysts through visual comparison with reference imagery to detect
    burned areas. Copernicus-EMS provided initial burned area estimates (1275 ha)
    as of 17 October 2019, which were supplemented by UNOSAT analysis identifying
    an additional 92 ha of burned surface by 19 October 2019.
  sources:
  - id: source_1
    license: null
    name: Copernicus-EMS
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wildfires-south-of-beirut-in-aley-and-chouf-districts-lebanon
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Burned area extent detected by satellite imagery in Aley and Chouf
      districts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Wildfires south of Beirut, in Aley and Chouf districts, Lebanon (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LB/FR20191016LBN/FR20191016LBN_gdb.zip
  format: Geodatabase
  id: resource_d22dce0b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20191016LBN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Wildfires south of Beirut, in Aley and Chouf districts, Lebanon (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LB/FR20191016LBN/FR20191016LBN_SHP.zip
  format: null
  id: resource_15aea98c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20191016LBN_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-lbn_unosat_wildfiressouthbeirutaleyc_20191021
spatial:
  bbox: null
  centroid: null
  countries:
  - LBN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-21'
temporal_resolution: null
title: Wildfires south of Beirut, in Aley and Chouf districts, Lebanon
version: null
vulnerability: null
---

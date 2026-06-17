---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-impact-analysis-in-bangio-village-pinogu-sub-district-bone-bolango-district-goro
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-bangio-village-pinogu-sub-district-bone-bolango-district-goro
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-bangio-village-pinogu-sub-district-bone-bolango-district-goro
dataset_id: rdls_hel-idn_unosat_landslideimpactanalysisba_20240716
description: 'UNOSAT code: LS20240708IDN This map illustrates satellite-detected landslides
  in Bangio Village, Pinogu Sub-District, Bone Bolango District, Gorontalo Province,
  Indonesia as observed from a Sentinel-2 image acquired on 14 July 2024 at 02:17
  UTC. Within the analysed area of 76 hectares, about 7 hectares of landslide scars
  were observed. UNITAR-UNOSAT identified 26 potentially affected structures. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/landslide-impact-analysis-in-bangio-village-pinogu-sub-district-bone-bolango-district-goro]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Building structures potentially affected by landslides in Bangio
      Village
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
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: landslide
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on 14
    July 2024 and compared it with reference imagery to identify landslide scars and
    delineate affected areas. Spatial analysis identified 26 potentially affected
    structures within the 76-hectare study area of Bangio Village. This preliminary
    assessment has not been validated through field surveys.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/landslide-impact-analysis-in-bangio-village-pinogu-sub-district-bone-bolango-district-goro
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Potentially affected structures identified through satellite analysis
      of landslide impact
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_1
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide impact analysis in Bangio Village, Pinogu Sub-District, Bone
    Bolango District, Gorontalo Province, Indonesia as of 14 July 2024. (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3899/LS20240708IDN.gdb.zip
  format: Geodatabase
  id: resource_f1a0672a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240708IDN.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide impact analysis in Bangio Village, Pinogu Sub-District, Bone
    Bolango District, Gorontalo Province, Indonesia as of 14 July 2024. (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3899/LS20240708IDN_SHP.zip
  format: null
  id: resource_14f0a641
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240708IDN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_unosat_landslideimpactanalysisba_20240716
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-07-16'
temporal_resolution: null
title: Landslide impact analysis in Bangio Village, Pinogu Sub-District, Bone Bolango
  District, Gorontalo Province, Indonesia as of 14 July 2024.
version: null
vulnerability: null
---

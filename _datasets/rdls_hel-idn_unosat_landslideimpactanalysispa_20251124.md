---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-impact-analysis-in-pandanarum-sub-district-banjarnegara-regency-jawa-tengah-prov
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-pandanarum-sub-district-banjarnegara-regency-jawa-tengah-prov
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-pandanarum-sub-district-banjarnegara-regency-jawa-tengah-prov
dataset_id: rdls_hel-idn_unosat_landslideimpactanalysispa_20251124
description: 'UNOSAT code: LS20251118IDN This map illustrates satellite-detected landslides
  in Pandanarum Sub-district, Banjarnegara Regency, Jawa Tengah Province, Indonesia
  as observed from a Sentinel-2 and Chaohu-1images acquired on 18 and 19 November
  2025. Within the analysed area of 500 hectares about 30 hectares of landslide scars
  were observed. UNITAR-UNOSAT identified about 70 damaged buildings and 60 potentially
  affected buildings. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-impact-analysis-in-pandanarum-sub-district-banjarnegara-regency-jawa-tengah-prov]'
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
    description: Building stock in the landslide-affected area, classified as damaged
      or potentially affected
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared Sentinel-2 and Chaohu-1 satellite imagery
    acquired on 18-19 November 2025 to detect landslide scars and assess building
    damage in Pandanarum Sub-district. Approximately 30 hectares of landslide scars
    were identified within a 500-hectare analysis area, with 70 damaged buildings
    and 60 potentially affected buildings mapped through visual interpretation. This
    preliminary analysis has not been field-validated.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
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
- href: https://data.humdata.org/dataset/landslide-impact-analysis-in-pandanarum-sub-district-banjarnegara-regency-jawa-tengah-prov
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from satellite-detected landslides
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings potentially affected by landslides
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide impact analysis in Pandanarum Sub-district, Banjarnegara
    Regency, Jawa Tengah Province, Indonesia as of 18 & 19 November 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4221/LS20251118IDN_gdb.zip
  format: Geodatabase
  id: resource_ae8d73ef
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20251118IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide impact analysis in Pandanarum Sub-district, Banjarnegara
    Regency, Jawa Tengah Province, Indonesia as of 18 & 19 November 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4221/LS20251118IDN_SHP.zip
  format: null
  id: resource_1a85ba79
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20251118IDN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_unosat_landslideimpactanalysispa_20251124
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
  start: '2025-11-24'
temporal_resolution: null
title: Landslide impact analysis in Pandanarum Sub-district, Banjarnegara Regency,
  Jawa Tengah Province, Indonesia as of 18 & 19 November 2025
version: null
vulnerability: null
---

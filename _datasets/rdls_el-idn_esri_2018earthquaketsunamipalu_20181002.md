---
attributions:
- entity:
    affiliation: null
    email: null
    name: DigitalGlobe
    url: https://data.humdata.org/dataset/digital-globe-palu-indonesia-oct-2
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Esri
  url: https://data.humdata.org/dataset/digital-globe-palu-indonesia-oct-2
creator:
  affiliation: null
  email: null
  name: Esri
  url: https://data.humdata.org/dataset/digital-globe-palu-indonesia-oct-2
dataset_id: rdls_el-idn_esri_2018earthquaketsunamipalu_20181002
description: 'Imagery captured by Digital Globe on 2 October 2018 of Palu, Indonesia.
  The data is available as a service https://www.arcgis.com/home/item.html?id=d0ff196041e04e0d8d3a09e1e435625d
  where the tiffs can also be downloaded.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/digital-globe-palu-indonesia-oct-2]'
details: https://www.digitalglobe.com/opendata/indonesia-earthquake-tsunami/post-event
  https://www.digitalglobe.com/opendata/indonesia-earthquake-tsunami/license
exposure:
- asset_type:
    description: Building footprints and structures in Palu visible in post-event
      satellite imagery
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
      quantity_kind: area
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event satellite imagery acquired by DigitalGlobe on 2 October
    2018 of Palu, Indonesia, providing visual documentation of building damage and
    urban impacts from the earthquake-tsunami event. The imagery is distributed as
    GeoTIFF files through ArcGIS services for damage assessment and loss quantification.
  sources:
  - id: source_1
    license: null
    name: DigitalGlobe
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/digital-globe-palu-indonesia-oct-2
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 2018 Palu earthquake-tsunami event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
    description: Direct building damage from the 2018 Palu tsunami
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: null
      trigger: null
      type: tsunami
    id: loss_2
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
  description: 'Indonesia: 2018 Earthquake-Tsunami in Palu (Palu Earthquake-Tsunami.lpkx)'
  download_url: https://data.humdata.org/dataset/88e41aff-5251-426b-b1e3-69944f499f64/resource/851558ce-d964-4785-a162-1431a0fc7ffc/download/palu-earthquake-tsunami.lpkx
  format: null
  id: resource_851558ce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Palu Earthquake-Tsunami.lpkx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: 2018 Earthquake-Tsunami in Palu (Palu Earthquake-Tsunami.lyrx)'
  download_url: https://data.humdata.org/dataset/88e41aff-5251-426b-b1e3-69944f499f64/resource/b009cbd8-f980-4f44-aa1c-207715562c80/download/palu-earthquake-tsunami.lyrx
  format: null
  id: resource_b009cbd8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Palu Earthquake-Tsunami.lyrx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-idn_esri_2018earthquaketsunamipalu_20181002
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
  start: '2018-10-02'
temporal_resolution: null
title: 'Indonesia: 2018 Earthquake-Tsunami in Palu'
version: null
vulnerability: null
---

---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: hillaryhanselim7@gmail.com
  name: Hilary_Mvungi
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1549
creator:
  affiliation: null
  email: hillaryhanselim7@gmail.com
  name: Hilary_Mvungi
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1549
dataset_id: rdls_he-tza_resilienceacade_daressalaamfloodhazardcur
description: 'Tanzania is the most flood-affected country in East Africa, with towns
  and cities undergoing massive spatial expansion with a growth in informal settlements.
  The flooding problem is compounded by limited access to adequate municipal services
  and infrastructure such as water supply, sanitation, solid waste, electricity and
  drainage. In response to these issues, the World Bank has formed a partnership with
  the UK Foreign, Commonwealth and Development Office, and the establishment of the
  Tanzania Urban Resilience Program (TURP). This 5-year trust fund with resources
  from the UK''s International Climate Fund for Bank executed activities to support
  climate resilience dialogue and training for Tanzanian cities and includes provision
  for recipient executed risk mitigation investments. TURP has been leading the preparation
  of financing for transformative flood control investments such as for Dar es Salaam''s
  Msimbazi River, as well as establishing the Resilience Academy to foster knowledge
  and information on urban resilience and initiate tools to aid decision-makers and
  stakeholders in managing risk The dashboard and analysis that it contains provides
  the Government and people of Dar es Salaam and Zanzibar with the evidence-based
  data, information and analysis tools to help reduce the negative impacts of flooding.
  The dashboard is intended to allow users to access, visualize and interrogate the
  hazard and risk data for Dar es Salaam and Zanzibar City.. [Source: This metadata
  record was automatically extracted from the GeoNode portal resilienceacademy]'
details: null
exposure:
- asset_type: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
- asset_type: null
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
  - analysis_type: probabilistic
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Official government dataset. Data quality maintained by the responsible
    government authority.
  sources:
  - id: source_1
    license: null
    name: Hilary_Mvungi
    risk_data_type:
    - hazard
    - exposure
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://crd.resilienceacademy.ac.tz/catalogue/#/dataset/747
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: kyondason
  url: https://geonode.resilienceacademy.ac.tz
purpose: In response to these issues, the World Bank has formed a partnership with
  the UK Foreign, Commonwealth and Development Office, and the establishment of the
  Tanzania Urban Resilience Program (TURP). This 5-year trust fund with resources
  from the UK's International Climate Fund for Bank executed activities to support
  climate resilience dialogue and training for Tanzanian cities and includes provision
  for recipient executed risk mitigation investments. TURP has been leading the preparation
  of financing for transformative flood control investments such as for Dar es Salaam's
  Msimbazi River, as well as establishing the Resilience Academy to foster knowledge
  and information on urban resilience and initiate tools to aid decision-makers and
  stakeholders in managing risk The dashboard and analysis that it contains provides
  the Government and people of Dar es Salaam and Zanzibar with the evidence-based
  data, information and analysis tools to help reduce the negative impacts of flooding.
  The dashboard is intended to allow users to access, visualize and interrogate the
  hazard and risk data for Dar es Salaam and Zanzibar City..
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32737
  description: Dar es Salaam flood hazard - Current
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__dsm_t1_t1000_reference_hazard_maps&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32737
  description: Dar es Salaam flood hazard - Current
  download_url: https://crd.resilienceacademy.ac.tz/api/v2/assets/155/link
  format: null
  id: resource_1
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dsm_t1_t1000_reference_hazard_maps
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:dsm_t1_t1000_reference_hazard_maps
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:32737
  description: 'Dar es Salaam flood hazard - Current (OGC WMS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:dsm_t1_t1000_reference_hazard_maps&format=image%2Fpng
  format: null
  id: resource_2
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:dsm_t1_t1000_reference_hazard_maps
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:32737
  description: 'Dar es Salaam flood hazard - Current (OGC WCS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:dsm_t1_t1000_reference_hazard_maps
  format: null
  id: resource_3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-tza_resilienceacade_daressalaamfloodhazardcur
spatial:
  bbox:
  - 465980.0001220703
  - 9202980.00012207
  - 564020.0001220703
  - 9283020.00012207
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2024
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Dar es Salaam flood hazard - Current
version: null
vulnerability: null
---

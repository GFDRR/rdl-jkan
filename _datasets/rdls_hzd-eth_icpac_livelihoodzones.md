---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net/api/v2/users/1001
creator:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net/api/v2/users/1001
dataset_id: rdls_hzd-eth_icpac_livelihoodzones
description: "Livelihood zone maps define geographic areas of a country where people\
  \ generally share similar options for obtaining food and income and similar access\
  \ to markets. An understanding of geographic livelihood systems is a key component\
  \ in Vulnerability Assesment for both Drought and Floods - The livelihood zones\
  \ of resolution approximately 5000 metres ( 0.05\xC3\u20140.05) Referenced September\
  \ 2019 [Source: This metadata record was automatically extracted from the GeoNode\
  \ portal icpac]"
details: null
exposure: []
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
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: IGAD DRM Team
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.icpac.net/layers/Normalized_Biomes:geonode:Normalized_Biomes
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net
purpose: 'component : Exposure Relationship to vulnerability component - Positive
  Zones in drought prone areas tend to be less vulnerable if they are characterized
  by multiple livelihood options (This is tied to other factors such as income levels).'
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:Normalized_Biomes
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Ethiopia Livelihood zones (OGC WMS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:Normalized_Biomes&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:Normalized_Biomes
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Ethiopia Livelihood zones (OGC WCS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:Normalized_Biomes
  format: null
  id: resource_1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-eth_icpac_livelihoodzones
spatial:
  bbox:
  - 33.083
  - 3.433
  - 47.933
  - 14.833
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2025
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Ethiopia Livelihood zones
version: null
vulnerability: null
---

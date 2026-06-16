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
dataset_id: rdls_exp-gha_icpac_ghapharmacies
description: 'Shows pharmacies in the East Africa Region Healthsites.io (The Global
  Healthsites Mapping Project) is a collaborative mapping project that aims to create
  a free, curated, global dataset of health facility locations and their service information.
  It integrates with OpenStreetMap (OSM), the world''s largest open geographic database.
  This theme includes all OpenStreetMap features in this area matching ( Learn what
  tags means here ) : tags[''healthcare''] IS NOT NULL OR tags[''amenity''] IN (''doctors'',
  ''dentist'', ''clinic'', ''hospital'', ''pharmacy'') Features may have these attributes:
  name name:en amenity building healthcare healthcare:speciality operator:type capacity:persons
  addr:full addr:city source name:sw This dataset is one of many OpenStreetMap exports
  on HDX. [Source: This metadata record was automatically extracted from the GeoNode
  portal icpac]'
details: null
exposure:
- asset_type: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: IGAD DRM Team
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.icpac.net/layers/icpac_geoportal_data:geonode:GHA_pharmacy
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net
purpose: null
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:GHA_pharmacy
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'GHA_pharmacies (OGC WMS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:GHA_pharmacy&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:GHA_pharmacy
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'GHA_pharmacies (OGC WFS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:GHA_pharmacy&outputFormat=application%2Fjson
  format: null
  id: resource_1
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: geonode Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gha_icpac_ghapharmacies
spatial:
  bbox:
  - 26.1285951
  - -10.7252411
  - 46.2210555
  - 15.7764378
  centroid: null
  countries:
  - GHA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2025
  duration: null
  end: null
  start: null
temporal_resolution: null
title: GHA_pharmacies
version: null
vulnerability: null
---

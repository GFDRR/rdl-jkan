---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/203
creator:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/203
dataset_id: rdls_he-nru_pacificdata_landuselandcovernauru2010
description: 'Land cover refers to the physical and biological cover over the surface
  of land, including water, vegetation, bare soil, and/or artificial structures. Land
  use usually refers to signs of human activities such as agriculture, forestry and
  building construction that altered the original land surface processes. The Land
  Use / Land Cover (LULC) maps were developed using remotely sensed data (i.e., satellite
  imagery) of different resolution and vintage and validated with the aid of some
  ground truthing, virtual truthing (using high-resolution imagery of more recent
  vintage and other internet resources), agriculture census, and other ancillary data
  collected during the course of the project. Preliminary interpretation of the Land
  Use / Land Cover (LULC) data from the satellite imagery was carried out by using
  an image classification algorithm and was enhanced by using imagery parameters such
  as tone, texture, pattern, size, shape and contextual association. This process
  was further improved using onscreen digitization of the known crops on high resolution
  satellite imagery. A Normalized Difference Vegetation Index (NDVI) was generated
  and used for classifying forest areas classification into dense, open, or shrub
  forests. Given the methodology adopted, it is to be expected that in some instances
  the information included in the LULC maps may be obsolete and inaccurate. The LULC
  maps developed are suitable for the scope of assessing wind and flood hazard (roughness
  factors and precipitation runoff percentages) as well establishing a crop exposure
  database. Data Sources: Publically available EO-1, LandSat imagery, partial coverage
  10m SPOT, others. Compiled by AIR Worldwide. [Source: This metadata record was automatically
  extracted from the GeoNode portal pacificdata]'
details: The detailed LULC map for Nauru was developed by AIR covers the main island.
  NASAs Earth observing - 1 (EO-1 ALI) data of 2010 were used. No actual field verification
  were done. However, virtual truthing was done using high resolution imagery Quick
  Bird (0.6 M) available to the team from SOPAC and other sources.
exposure:
- asset_type: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: empirical
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
license: https://creativecommons.org/licenses/by-nc-sa/4.0/
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: Earth and Oceans Observations Team Pacific Community
    risk_data_type:
    - hazard
    - exposure
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geonode.pacificdata.org/catalogue/#/dataset/203
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Land use / Land cover for Nauru 2010 (JSON)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Anauru_vector&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_0
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Land use / Land cover for Nauru 2010 (GML 3.1.1)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Anauru_vector&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_1
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 3.1.1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Land use / Land cover for Nauru 2010 (Zipped Shapefile)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Anauru_vector&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Land use / Land cover for Nauru 2010 (CSV)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Anauru_vector&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CSV
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Land use / Land cover for Nauru 2010 (Excel)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Anauru_vector&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Land use / Land cover for Nauru 2010 (GML 2.0)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Anauru_vector&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_5
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 2.0
- access_url: https://geonode.pacificdata.org/datasets/geonode:nauru_vector
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Land use / Land cover for Nauru 2010 (OGC WMS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:nauru_vector&format=image%2Fpng
  format: null
  id: resource_6
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.pacificdata.org/datasets/geonode:nauru_vector
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Land use / Land cover for Nauru 2010 (OGC WFS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:nauru_vector&outputFormat=application%2Fjson
  format: null
  id: resource_7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: geonode Service'
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-nru_pacificdata_landuselandcovernauru2010
spatial:
  bbox:
  - 166.90754792760887
  - -0.557344495985478
  - 166.96245701851794
  - -0.499526314167319
  centroid: null
  countries:
  - NRU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2020
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Land use / Land cover for Nauru 2010
version: null
vulnerability: null
---
